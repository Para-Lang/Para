# coding=utf-8
""" Test for the compiler process setup """
import os
import paraccompiler

from . import reset_input

main_file_path = f"{os.getcwd()}\\test_files\\main.para"


class TestProcess:
    def teardown_method(self, method):
        """ This method is being called after each test case, and it will revert input back to the original function """
        reset_input()

    def test_init(self):
        b_path = f"{os.getcwd()}\\build\\"
        d_path = f"{os.getcwd()}\\dist\\"
        p = paraccompiler.CompilationProcess.create_from_args(main_file_path, b_path, d_path)

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_bytes_init(self):
        path = main_file_path.encode()

        b_path = f"{os.getcwd()}\\build\\".encode()
        d_path = f"{os.getcwd()}\\dist\\".encode()
        p = paraccompiler.CompilationProcess.create_from_args(path, b_path, d_path)

        assert p.build_path == b_path.decode()
        assert p.dist_path == d_path.decode()