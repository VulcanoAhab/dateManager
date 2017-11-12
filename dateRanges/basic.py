import calendar
import datetime
import collections

class BaseRange:
    """
    """

    _dateRange=0

    def __init__(self, init, end, inFormat, outFormat=None):
        """
        """
        self._inFormat=inFormat
        self._outFormat=outFormat if outFormat else self._inFormat
        self._init=datetime.datetime.strptime(init, self._inFormat)
        self._end=datetime.datetime.strptime(end, self._inFormat)
        self._maxDays=(self._end-self._init).days

    def buildRanges(self, reverse=False):
        """
        """
        sizis=self._dateRange
        resultRange=collections.namedtuple("DateRange", ["init", "end"])
        rangis=range(sizis,(self._end-self._init).days,sizis)
        for n,week in enumerate(rangis):
            nextDate=self._init+datetime.timedelta(days=week)
            if n == 0:
                init=self._init
                end=nextDate
            else:
                init=nextDate
                end=nextDate+datetime.timedelta(days=self._dateRange)
            yield resultRange(init.strftime(self._outFormat),
                              end.strftime(self._outFormat))


class Weekly(BaseRange):
    """
    """

    _dateRange=7

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)

class Monthly(BaseRange):
    """
    """

    _dateRange=30

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)
