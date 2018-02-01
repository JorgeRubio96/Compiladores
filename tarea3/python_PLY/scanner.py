from sre_parse import Pattern, SubPattern, parse
from sre_compile import compile as sre_compile
from sre_constants import BRANCH, SUBPATTERN


class Scanner(object):

    def __init__(self, rules, flags=0):
        pattern = Pattern()
        pattern.flags = flags
        pattern.groups = len(rules) + 1

        self.rules = [name for name, _ in rules]
        self._scanner = sre_compile(SubPattern(pattern, [
            (BRANCH, (None, [SubPattern(pattern, [
                (SUBPATTERN, (group, parse(regex, flags, pattern))),
            ]) for group, (_, regex) in enumerate(rules, 1)]))
        ])).scanner

    def scan(self, string, skip=False):
        sc = self._scanner(string)

        match = None
        for match in iter(sc.search if skip else sc.match, None):
            yield self.rules[match.lastindex - 1], match

        if not skip and not match or match.end() < len(string):
            raise EOFError(match.end())