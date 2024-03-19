#!/usr/bin/env python3

from logger import Logger


Logger = Logger()

def test_info(info: str):
    Logger.log_info(info)


def test_warn(warn: str):
    Logger.log_warning(warn)


def test_err(err: str):
    Logger.log_err(err)


def test_crit(crit: str):
    Logger.log_critical(crit)



def test_division(x, y):
    try:
        res = x / y
        test_info(f"x/y successful with {res}")

    except Exception as e:
        test_err(e)


if __name__ == "__main__":
    test_division(15, 3)
    test_division(1, 0)
