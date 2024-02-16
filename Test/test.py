import os
import sys
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.dirname(dir)
sys.path.insert(1, dir)
from TestHelp.testHelp import *
from TestAssist.testAssist import *
from TestEvent.testEvent import *
from TestMember.testMember import *
from TestRange.testRange import *
from TestPointMember.testPointMember import *
from TestAllPointMember.testAllPointMember import *
from TestConstraints.testConstraints import *