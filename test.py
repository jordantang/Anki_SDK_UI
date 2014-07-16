#!/usr/bin/python

import SDK
import sys
import getopt
import time

def main(argv=None):
  SDK.ANKI_start();
  time.sleep(5);
  SDK.ANKI_end();

main()
