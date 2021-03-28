import simple_gsd_lcm

class TestSimple():
    def test_8(self):
        assert simple_gsd_lcm.simple(8) == 'Число не простое'

    def test_5(self):
        assert simple_gsd_lcm.simple(5) == 'Число простое'

class TestGcd():
    def test_36_48(self):
        assert simple_gsd_lcm.gcd(36, 48) == 12

    def test_28_35(self):
        assert simple_gsd_lcm.gcd(28, 35) == 7

class TestLcm():
    def test_36_48(self):
        assert simple_gsd_lcm.lcm(0, 35) == 0

    def test_28_35(self):
        assert simple_gsd_lcm.lcm(28, 35) == 140
