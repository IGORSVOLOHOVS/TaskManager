import os, subprocess, webbrowser

def gen_docs():
    print("📚 Docs & UML...")
    cfg = """
    PROJECT_NAME           = "CppSconExample"
    OUTPUT_DIRECTORY       = docs
    GENERATE_LATEX         = NO
    HAVE_DOT               = YES
    UML_LOOK               = YES
    CALL_GRAPH             = YES
    EXTRACT_ALL            = YES
    RECURSIVE              = YES
    INPUT                  = .
    EXCLUDE_PATTERNS       = */build/* */.git/* */.ipynb_checkpoints/*
    """

    try:
        subprocess.run(["doxygen", "-"], input=cfg, text=True, stderr=subprocess.DEVNULL, check=True)
        
        path = os.path.join("docs", "html", "index.html")
        if os.path.exists(path):
            print(f"🌍 Open: {path}")
            webbrowser.open(f"file://{os.path.abspath(path)}")
        else:
            print(f"⚠️ Index not found: {path}")
            
    except FileNotFoundError:
        print("❌ Error: Doxygen not installed (try: sudo apt install doxygen graphviz)")
    except subprocess.CalledProcessError:
        print("❌ Error: Doxygen returned non-zero exit code")
