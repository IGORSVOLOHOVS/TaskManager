#ifndef BACKEND_H
#define BACKEND_H

#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QObject>
#include <QDebug>

class Backend : public QObject
{
    Q_OBJECT
public:
    static void registerType() {
        qmlRegisterType<Backend>("Backend", 1, 0, "Backend");
    }

    explicit Backend(QObject *parent = nullptr) : QObject(parent) {}

signals:
    void dataProcessed(const QString &result);

public slots:
    QString process(const QString &input) {
        QString result = input.toUpper();
        emit dataProcessed(result);
        return result;
    }

    QString multiplyText(const QString &text, int times) {
        return text.repeated(times);
    }

    void logValues(const QString &message, double number, bool flag) {
        qDebug() << "[C++]" << message << number << flag;
    }
};

#endif // BACKEND_H
