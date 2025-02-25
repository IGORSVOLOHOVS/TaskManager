import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import QtQuick.Layouts 1.15
import Backend 1.0

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "Professional QML Demo"
    minimumWidth: 600
    minimumHeight: 400

    // Material Design конфигурация
    Material.theme: Material.Light
    Material.accent: Material.Purple
    Material.primary: Material.Indigo

    // Загрузка кастомного шрифта
    FontLoader {
        id: customFont
        source: "fonts/Roboto-Regular.ttf"
    }

    // Бэкенд
    Backend {
        id: backend
        onDataProcessed: resultLabel.text = "Async result: " + result
    }

    // Боковое меню
    Drawer {
        id: drawer
        width: 0.3 * parent.width
        height: parent.height

        ColumnLayout {
            width: parent.width
            spacing: 10

            Label {
                text: "Меню"
                font.bold: true
                font.pixelSize: 18
                Layout.alignment: Qt.AlignCenter
            }

            Button {
                text: "Настройки"
                Layout.fillWidth: true
                font.pixelSize: 14
                onClicked: swipeView.currentIndex = 1
            }

            Button {
                text: "О программе"
                Layout.fillWidth: true
                font.pixelSize: 14
                onClicked: swipeView.currentIndex = 2
            }
        }
    }

    // Основной интерфейс
    SwipeView {
        id: swipeView
        anchors.fill: parent
        interactive: false

        // Главная страница
        Page {
            ColumnLayout {
                anchors.centerIn: parent
                spacing: 20

                Label {
                    id: resultLabel
                    text: "Нажмите кнопки для взаимодействия"
                    font.pixelSize: 18
                    Layout.alignment: Qt.AlignCenter
                }

                ProgressBar {
                    id: progressBar
                    value: 0.5
                    Layout.preferredWidth: 300
                }

                GridLayout {
                    columns: 2
                    columnSpacing: 20
                    rowSpacing: 15

                    Button {
                        text: "Обработать текст"
                        Layout.preferredWidth: 200
                        font.pixelSize: 14
                        onClicked: {
                            const res = backend.process("hello world")
                            console.log("Результат:", res)
                        }
                    }

                    Button {
                        text: "Умножить текст"
                        Layout.preferredWidth: 200
                        font.pixelSize: 14
                        onClicked: {
                            const result = backend.multiplyText("QML", 3)
                            resultLabel.text = "Умножено: " + result
                        }
                    }

                    Button {
                        text: "Логирование"
                        Layout.preferredWidth: 200
                        font.pixelSize: 14
                        onClicked: {
                            backend.logValues("Значение:", Math.random(), true)
                        }
                    }

                    Button {
                        text: "Смешанные параметры"
                        Layout.preferredWidth: 200
                        font.pixelSize: 14
                        onClicked: {
                            backend.process("Время: " + Date.now())
                            backend.multiplyText("!", Math.floor(Math.random() * 10))
                        }
                    }
                }

                // Переключатель темы
                RowLayout {
                    Layout.alignment: Qt.AlignCenter
                    spacing: 10

                    Label {
                        text: "Тёмная тема"
                        font.pixelSize: 14
                    }

                    Switch {
                        checked: Material.theme === Material.Dark
                        onClicked: Material.theme = checked ? Material.Dark : Material.Light
                    }
                }
            }
        }

        // Страница настроек
        Page {
            Label {
                anchors.centerIn: parent
                text: "Страница настроек"
                font.pixelSize: 24
            }
        }

        // Страница "О программе"
        Page {
            Label {
                anchors.centerIn: parent
                text: "Профессиональное QML-приложение\nВерсия 1.0.0"
                font.pixelSize: 24
                horizontalAlignment: Text.AlignHCenter
            }
        }
    }

    // Футер
    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

        TabButton {
            text: "Главная"
            onClicked: swipeView.currentIndex = 0
        }

        TabButton {
            text: "Настройки"
            onClicked: swipeView.currentIndex = 1
        }

        TabButton {
            text: "О программе"
            onClicked: swipeView.currentIndex = 2
        }
    }

    // Анимации
    Behavior on Material.primary {
        ColorAnimation { duration: 300 }
    }
}
