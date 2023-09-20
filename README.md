# TaskManager 3.0v

## Description

TaskManager 3.0v is a Windows Batch script designed to automatically clone a specific GitHub repository and copy a particular folder within it to a specified location on your local machine. The copied folder is renamed to include the current date and time for easier identification.

## Features

- Automatically clones a GitHub repository to a temporary directory.
- Copies a specific folder (`TaskTools`) from the cloned repository to a designated directory.
- Renames the copied folder to include the current date and time, down to the seconds for uniqueness.

## Requirements

- Windows Operating System
- Git installed and accessible from the Command Line

## Installation

1. Download the `TaskManager.bat` script from the GitHub repository.
2. Place the `.bat` file in a directory where you wish to run it from.

## Usage

1. Open a Command Prompt as an administrator.
2. Navigate to the directory where `TaskManager.bat` is located.
3. Run the script:

   ```
   TaskManager.bat
   ```

The script will clone the repository, copy the `TaskTools` folder, and rename it to a folder that includes the current date and time in `C:\Users\User\Projects`.

## How It Works

Here is a quick overview of what each section of the code does:

```batch
:: Получаем текущую дату и время
:: Gets the current date and time.
```

```batch
:: Установка путей
:: Sets up the URLs and directory paths.
```

```batch
:: Клонирование репозитория
:: Clones the GitHub repository.
```

```batch
:: Копирование папки TaskTools в целевую директорию
:: Copies the TaskTools folder to the target directory.
```

```batch
:: Удаление временной папки с клоном репозитория
:: Removes the temporary directory where the repository was cloned.
```
