import os, subprocess, sys, shutil, webbrowser

root_dir = os.getcwd()

##
# @brief Определяет версию компилятора.
def get_ver(cc):
    try:
        r = subprocess.run([cc, '-dumpfullversion'], capture_output=True, text=True)
        if r.returncode == 0: return r.stdout.strip()
        r = subprocess.run([cc, '--version'], capture_output=True, text=True)
        return r.stdout.split("version ")[1].split()[0] if "version" in r.stdout else "0.0"
    except: return "0.0"

##
# @brief Единый пайплайн с ДЕТАЛЬНЫМИ логами ошибок.
def run_pipeline(cfg):
    ver = get_ver(cfg['cc'])
    suffix = "-cov" if 'cov_flags' in cfg else ""
    v_name = f"{cfg['name']}-{ver}-{cfg['type']}-{cfg['flags'].replace(' ', '_')}{suffix}"
    
    b_dir = os.path.join(root_dir, "build", v_name)
    if not os.path.exists(b_dir): os.makedirs(b_dir); print(f"📂 Created: {v_name}")

    full_cflags = f"{cfg.get('flags', '')} {cfg.get('cov_flags', '')}"
    full_lflags = cfg.get('cov_flags', '')

    # SCons: Подключаем заголовки и исходники
    # Важно: VariantDir дублирует иерархию src в папку build, чтобы не мусорить в src
    sc = f"env=Environment(CXX='{cfg['cc']}');" \
         f"env.Append(CXXFLAGS='{full_cflags}', LINKFLAGS='{full_lflags}');" \
         f"env.Append(CPPPATH=['../../include']);" \
         f"VariantDir('.', '../../src', duplicate=0);" \
         f"env.Program('main', source=Glob('*.cpp'))"
    
    with open(os.path.join(b_dir, "SConstruct"), "w") as f: f.write(sc)

    print(f"🔨 Build: {v_name}...")
    
    # --- ИЗМЕНЕНИЕ: Захват и вывод логов ---
    # Запускаем SCons
    proc = subprocess.run(["scons", "-j4"], cwd=b_dir, capture_output=True, text=True)
    
    if proc.returncode != 0:
        print(f"❌ Build Failed in {b_dir}")
        print("🔻🔻🔻 LOGS START 🔻🔻🔻")
        print(proc.stdout) # Стандартный вывод (обычно ошибки компиляции здесь)
        print(proc.stderr) # Ошибки системы сборки
        print("🔺🔺🔺 LOGS END 🔺🔺🔺")
        return # Прерываем выполнение для этой конфигурации
    # ---------------------------------------
    
    bin_p = os.path.join(b_dir, "main")
    if not os.path.exists(bin_p): return print("❌ Binary missing (Success reported but file not found?)")

    print(f"🚀 Run: {os.path.basename(bin_p)}")
    
    # Запуск бинарника
    run_proc = subprocess.run([bin_p], cwd=b_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if 'cov_flags' not in cfg:
        print(run_proc.stdout) # Показываем вывод программы, если это не тест покрытия
    
    if run_proc.returncode != 0:
        print(f"⚠️ Runtime Error: {run_proc.stderr}")

    # --- COVERAGE ---
    if 'cov_tool' in cfg:
        print("📊 Generating Coverage Report...")
        try:
            info, html = os.path.join(b_dir, "cov.info"), os.path.join(b_dir, "html")
            
            # Флаги для подавления ошибок (GCC 15+ часто требует этого)
            ignore_flags = ['--ignore-errors', 'mismatch,mismatch'] # Удвоенный mismatch как в логе
            rc_flags = ['--rc', 'branch_coverage=1']

            # 1. Сбор данных (Scan)
            # Тут консоль может всё ещё выдать WARNING, это нормально — мы их отфильтруем ниже
            subprocess.run(
                [cfg['cov_tool'], '-c', '-d', b_dir, '-o', info] + rc_flags + ignore_flags, 
                stdout=subprocess.DEVNULL, check=True
            )
            
            # 2. Очистка: ЯВНО удаляем системные файлы (/usr/include и т.д.)
            subprocess.run(
                [cfg['cov_tool'], '--remove', info, '/usr/*', '-o', info] + rc_flags + ignore_flags,
                stdout=subprocess.DEVNULL, check=True
            )

            # 3. Фильтрация: Оставляем только то, что внутри папки src
            subprocess.run(
                [cfg['cov_tool'], '--extract', info, '*/src/*', '-o', info] + rc_flags + ignore_flags,
                stdout=subprocess.DEVNULL, check=True
            )

            # 4. Генерация HTML
            subprocess.run(['genhtml', info, '-o', html, '--branch-coverage'], stdout=subprocess.DEVNULL, check=True)
            
            idx = os.path.join(html, "index.html")
            if os.path.exists(idx): 
                print(f"🌍 Open: {idx}")
                webbrowser.open(f"file://{os.path.abspath(idx)}")
        except Exception as e:
            print(f"⚠️ Coverage Error: {e}")

def clean(target="all"):
    if target == "all":
        if os.path.exists("build"):
            shutil.rmtree("build")
            print("🧹 Build directory removed.")
    else:
        # Логика удаления конкретной папки (например, по имени варианта)
        pass

# def save_and_upload_builder_github():