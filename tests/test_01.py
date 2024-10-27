class TestClassDemoInstance:
    """Showing that each test takes a new instance of the test class"""
    value = 0

    def test_one(self):
        # This test passes
        self.value = 1
        assert self.value == 1

    def test_two(self):
        # This test fails
        assert self.value == 1
