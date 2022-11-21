moduleName = "fyersLog"

try:
    import datetime as dt
    from datetime import datetime, timezone
except Exception as e:
    print("moduleName: {}, ERR: could not import module : {}".format(moduleName,e))


class FyersLog:
    def __init__(self,logPath):
        self.logPath = logPath
        self.todayDate = str(dt.date.today())

    def logEntryFunc(self, timestamp, funcName, params, response, *logArgs):
        try:
            logArgsList = "\n{} :: {} :: {} :: {} :: {}\n".format(
                timestamp, funcName, params, str(int(datetime.now(tz=timezone.utc).timestamp() * 1000)), response)
            for i in logArgs:
                data = str(i)
                logArgsList += data
            filePointer = open("{}/{}{}".format(self.logPath, self.todayDate, ".txt"), "a")

            filePointer.write(logArgsList)
            filePointer.close()

        except Exception as e:
            print('ERR: logEntryFunc: {} : {}'.format(funcName, e))
            return