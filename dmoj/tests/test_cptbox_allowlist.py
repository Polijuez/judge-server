import unittest

from dmoj.cptbox.handlers import ALLOW
from dmoj.cptbox.isolate import IsolateTracer
from dmoj.cptbox.syscalls import by_id, sys_get_mempolicy, sys_mbind, sys_rseq, sys_set_mempolicy

# GHC's runtime queries and sets the NUMA policy as it starts up, so the HASK executor faults on
# syscall 239 and is never registered unless cptbox allows these two.
MEMPOLICY_SYSCALLS = (sys_get_mempolicy, sys_set_mempolicy)


class AllowlistTest(unittest.TestCase):
    def setUp(self):
        self.tracer = IsolateTracer(read_fs=[], write_fs=[])

    def test_mempolicy_syscalls_are_allowed(self):
        for syscall in MEMPOLICY_SYSCALLS:
            self.assertIn(syscall, self.tracer, f'{by_id[syscall]} is missing from the allowlist')
            self.assertEqual(self.tracer[syscall], ALLOW)

    def test_neighbouring_numa_syscalls_stay_denied(self):
        # Adding the two mempolicy calls must not open up the rest of the NUMA API.
        self.assertNotIn(sys_mbind, self.tracer)
        self.assertIn(sys_rseq, self.tracer)
