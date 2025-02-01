#if defined(_WIN32) || defined(_WIN64)
   #include <iostream>
    #include <fstream>
    #include <chrono>
    #include <iomanip>
    #include <sstream>
    #include <filesystem>
    #include <cstdlib>

    namespace fs = std::filesystem;

    int main() {
        // Получение текущей даты и времени
        auto now = std::chrono::system_clock::now();
        auto in_time_t = std::chrono::system_clock::to_time_t(now);
        std::stringstream ss;
        ss << std::put_time(std::localtime(&in_time_t), "%Y%m%d-%H%M%S");
        std::string datestamp = ss.str();

        // Установка путей
        std::string repoURL = "https://github.com/IGORSVOLOHOVS/TaskManager.git";
        std::string cloneDir = fs::temp_directory_path().string() + "\\" + datestamp;
        std::string targetDir = "C:\\Users\\User\\Projects\\Task-" + datestamp;

        // Клонирование репозитория
        std::string cloneCmd = "git clone -n --depth=1 --filter=tree:0 " + repoURL + " \"" + cloneDir + "\"";
        system(cloneCmd.c_str());

        // Переход в директорию репозитория и настройка sparse-checkout
        fs::current_path(cloneDir);
        system("git sparse-checkout set --no-cone TaskTools");
        system("git checkout");

        // Копирование папки TaskTools в целевую директорию
        fs::copy(cloneDir + "\\TaskTools", targetDir, fs::copy_options::recursive);

        // Иницифлизируем репозиторий в целевой директории(git init)
        fs::current_path(targetDir);
        system("git init");

        // Открытие целевой директории в VS Code (если VS Code установлен)
        std::string openCmd = "code \"" + targetDir + "\"";
        system(openCmd.c_str());

        // Удаление временной папки с клоном репозитория
        fs::remove_all(cloneDir);

        return 0;
    }
#else
 #include <iostream>
    #include <fstream>
    #include <chrono>
    #include <iomanip>
    #include <sstream>
    #include <filesystem>
    #include <cstdlib>

    namespace fs = std::filesystem;

    int main() {
        // Получение текущей даты и времени
        auto now = std::chrono::system_clock::now();
        auto in_time_t = std::chrono::system_clock::to_time_t(now);
        std::stringstream ss;
        ss << std::put_time(std::localtime(&in_time_t), "%Y%m%d-%H%M%S");
        std::string datestamp = ss.str();

        // Установка путей
        std::string repoURL = "https://github.com/IGORSVOLOHOVS/TaskManager.git";
        std::string cloneDir = fs::temp_directory_path().string() + "/" + datestamp;
        std::string targetDir = "/home/igors/Projects/Task-" + datestamp;

        // Create directory
        std::filesystem::create_directory(targetDir);

        // Клонирование репозитория
        std::string cloneCmd = "git clone -n --depth=1 --filter=tree:0 " + repoURL + " \"" + cloneDir + "\"";
        system(cloneCmd.c_str());

        // Переход в директорию репозитория и настройка sparse-checkout
        fs::current_path(cloneDir);
        system("git sparse-checkout set --no-cone TaskTools");
        system("git checkout");

        // Копирование папки TaskTools в целевую директорию
        fs::copy(cloneDir + "/TaskTools", targetDir, fs::copy_options::recursive);

        // Иницифлизируем репозиторий в целевой директории(git init)
        fs::current_path(targetDir);
        system("git init");

        // Открытие целевой директории в VS Code (если VS Code установлен)
        std::string openCmd ="code " + targetDir;
        system(openCmd.c_str());

        // Удаление временной папки с клоном репозитория
        fs::remove_all(cloneDir);

        return 0;
    }
#endif
