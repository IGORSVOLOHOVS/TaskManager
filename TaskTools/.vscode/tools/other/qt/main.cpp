#include "task.hpp"

using namespace task;

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    // Регистрация типа в QML
    Backend::registerType();

    QQmlApplicationEngine engine;
    QObject::connect(
        &engine,
        &QQmlApplicationEngine::objectCreationFailed,
        &app,
        []() { QCoreApplication::exit(-1); },
        Qt::QueuedConnection);
    engine.loadFromModule("untitled1", "Main");

    return app.exec();
}
