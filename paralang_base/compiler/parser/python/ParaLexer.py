# Generated from ./Para.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,70,725,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,2,88,7,88,2,89,7,89,2,90,7,90,2,
        91,7,91,2,92,7,92,2,93,7,93,2,94,7,94,2,95,7,95,2,96,7,96,2,97,7,
        97,2,98,7,98,2,99,7,99,2,100,7,100,2,101,7,101,2,102,7,102,2,103,
        7,103,2,104,7,104,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,
        1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,33,1,33,
        1,34,1,34,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,39,
        1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,
        1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,49,
        1,50,1,50,1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,1,54,
        1,54,1,54,1,55,1,55,1,56,1,56,1,56,1,57,1,57,1,58,1,58,1,58,1,59,
        1,59,1,60,1,60,1,60,5,60,441,8,60,10,60,12,60,444,9,60,1,61,1,61,
        5,61,448,8,61,10,61,12,61,451,9,61,1,61,1,61,1,62,1,62,3,62,457,
        8,62,1,63,1,63,1,64,1,64,1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,65,
        1,65,1,65,3,65,473,8,65,1,66,1,66,1,66,1,66,1,66,1,67,1,67,3,67,
        482,8,67,1,67,1,67,3,67,486,8,67,1,67,1,67,3,67,490,8,67,1,67,3,
        67,493,8,67,1,68,1,68,1,68,4,68,498,8,68,11,68,12,68,499,1,69,1,
        69,5,69,504,8,69,10,69,12,69,507,9,69,1,70,1,70,5,70,511,8,70,10,
        70,12,70,514,9,70,1,71,1,71,4,71,518,8,71,11,71,12,71,519,1,72,1,
        72,1,72,1,73,1,73,1,74,1,74,1,75,1,75,1,76,1,76,3,76,533,8,76,1,
        76,1,76,1,76,1,76,1,76,3,76,540,8,76,1,76,1,76,3,76,544,8,76,3,76,
        546,8,76,1,77,1,77,1,78,1,78,1,79,1,79,1,79,1,79,3,79,556,8,79,1,
        80,1,80,3,80,560,8,80,1,81,1,81,3,81,564,8,81,1,81,3,81,567,8,81,
        1,81,1,81,1,81,3,81,572,8,81,3,81,574,8,81,1,82,1,82,1,82,3,82,579,
        8,82,1,82,1,82,3,82,583,8,82,1,83,3,83,586,8,83,1,83,1,83,1,83,1,
        83,1,83,3,83,593,8,83,1,84,1,84,3,84,597,8,84,1,84,1,84,1,85,1,85,
        1,86,4,86,604,8,86,11,86,12,86,605,1,87,3,87,609,8,87,1,87,1,87,
        1,87,1,87,1,87,3,87,616,8,87,1,88,1,88,3,88,620,8,88,1,88,1,88,1,
        89,4,89,625,8,89,11,89,12,89,626,1,90,1,90,1,91,1,91,1,91,1,91,1,
        92,4,92,636,8,92,11,92,12,92,637,1,93,1,93,3,93,642,8,93,1,94,1,
        94,1,94,1,94,3,94,648,8,94,1,95,1,95,1,95,1,96,1,96,1,96,3,96,656,
        8,96,1,96,3,96,659,8,96,1,97,1,97,1,97,1,97,4,97,665,8,97,11,97,
        12,97,666,1,98,1,98,1,98,3,98,672,8,98,1,98,1,98,1,99,1,99,3,99,
        678,8,99,1,99,1,99,1,100,4,100,683,8,100,11,100,12,100,684,1,101,
        1,101,1,101,1,101,1,101,1,101,1,101,3,101,694,8,101,1,102,4,102,
        697,8,102,11,102,12,102,698,1,102,1,102,1,103,1,103,1,103,1,103,
        5,103,707,8,103,10,103,12,103,710,9,103,1,103,1,103,1,103,1,103,
        1,103,1,104,1,104,3,104,719,8,104,1,104,3,104,722,8,104,1,104,1,
        104,1,708,0,105,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,
        11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,
        22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,
        33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,
        44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,107,
        54,109,55,111,56,113,57,115,58,117,59,119,60,121,61,123,0,125,0,
        127,0,129,0,131,0,133,0,135,62,137,0,139,0,141,0,143,0,145,0,147,
        0,149,0,151,0,153,0,155,0,157,0,159,0,161,63,163,0,165,0,167,0,169,
        0,171,0,173,64,175,0,177,0,179,0,181,0,183,65,185,0,187,0,189,0,
        191,0,193,0,195,0,197,66,199,67,201,0,203,0,205,68,207,69,209,70,
        1,0,19,1,0,0,65534,3,0,65,90,95,95,97,122,1,0,48,57,2,0,66,66,98,
        98,1,0,48,49,2,0,88,88,120,120,1,0,49,57,1,0,48,55,3,0,48,57,65,
        70,97,102,2,0,85,85,117,117,2,0,76,76,108,108,2,0,69,69,101,101,
        2,0,43,43,45,45,2,0,80,80,112,112,4,0,70,70,76,76,102,102,108,108,
        4,0,10,10,13,13,39,39,92,92,10,0,34,34,39,39,63,63,92,92,97,98,102,
        102,110,110,114,114,116,116,118,118,4,0,10,10,13,13,34,34,92,92,
        2,0,9,9,32,32,744,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,
        0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,
        0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,
        0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,
        0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,
        0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,
        0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,
        0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,
        0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,
        0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,
        0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,
        117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,135,1,0,0,0,0,161,1,0,
        0,0,0,173,1,0,0,0,0,183,1,0,0,0,0,197,1,0,0,0,0,199,1,0,0,0,0,205,
        1,0,0,0,0,207,1,0,0,0,0,209,1,0,0,0,1,211,1,0,0,0,3,214,1,0,0,0,
        5,219,1,0,0,0,7,221,1,0,0,0,9,223,1,0,0,0,11,225,1,0,0,0,13,229,
        1,0,0,0,15,236,1,0,0,0,17,241,1,0,0,0,19,247,1,0,0,0,21,250,1,0,
        0,0,23,257,1,0,0,0,25,262,1,0,0,0,27,270,1,0,0,0,29,276,1,0,0,0,
        31,285,1,0,0,0,33,288,1,0,0,0,35,294,1,0,0,0,37,297,1,0,0,0,39,302,
        1,0,0,0,41,306,1,0,0,0,43,311,1,0,0,0,45,318,1,0,0,0,47,324,1,0,
        0,0,49,330,1,0,0,0,51,334,1,0,0,0,53,341,1,0,0,0,55,347,1,0,0,0,
        57,354,1,0,0,0,59,361,1,0,0,0,61,363,1,0,0,0,63,365,1,0,0,0,65,367,
        1,0,0,0,67,369,1,0,0,0,69,371,1,0,0,0,71,373,1,0,0,0,73,375,1,0,
        0,0,75,378,1,0,0,0,77,380,1,0,0,0,79,383,1,0,0,0,81,385,1,0,0,0,
        83,387,1,0,0,0,85,389,1,0,0,0,87,392,1,0,0,0,89,395,1,0,0,0,91,398,
        1,0,0,0,93,400,1,0,0,0,95,402,1,0,0,0,97,404,1,0,0,0,99,407,1,0,
        0,0,101,410,1,0,0,0,103,413,1,0,0,0,105,416,1,0,0,0,107,419,1,0,
        0,0,109,422,1,0,0,0,111,425,1,0,0,0,113,427,1,0,0,0,115,430,1,0,
        0,0,117,432,1,0,0,0,119,435,1,0,0,0,121,437,1,0,0,0,123,445,1,0,
        0,0,125,456,1,0,0,0,127,458,1,0,0,0,129,460,1,0,0,0,131,472,1,0,
        0,0,133,474,1,0,0,0,135,492,1,0,0,0,137,494,1,0,0,0,139,501,1,0,
        0,0,141,508,1,0,0,0,143,515,1,0,0,0,145,521,1,0,0,0,147,524,1,0,
        0,0,149,526,1,0,0,0,151,528,1,0,0,0,153,545,1,0,0,0,155,547,1,0,
        0,0,157,549,1,0,0,0,159,555,1,0,0,0,161,559,1,0,0,0,163,573,1,0,
        0,0,165,575,1,0,0,0,167,592,1,0,0,0,169,594,1,0,0,0,171,600,1,0,
        0,0,173,603,1,0,0,0,175,615,1,0,0,0,177,617,1,0,0,0,179,624,1,0,
        0,0,181,628,1,0,0,0,183,630,1,0,0,0,185,635,1,0,0,0,187,641,1,0,
        0,0,189,647,1,0,0,0,191,649,1,0,0,0,193,652,1,0,0,0,195,660,1,0,
        0,0,197,668,1,0,0,0,199,675,1,0,0,0,201,682,1,0,0,0,203,693,1,0,
        0,0,205,696,1,0,0,0,207,702,1,0,0,0,209,721,1,0,0,0,211,212,5,61,
        0,0,212,213,5,62,0,0,213,2,1,0,0,0,214,215,5,105,0,0,215,216,5,110,
        0,0,216,217,5,105,0,0,217,218,5,116,0,0,218,4,1,0,0,0,219,220,5,
        59,0,0,220,6,1,0,0,0,221,222,5,63,0,0,222,8,1,0,0,0,223,224,5,58,
        0,0,224,10,1,0,0,0,225,226,5,46,0,0,226,227,5,46,0,0,227,228,5,46,
        0,0,228,12,1,0,0,0,229,230,5,105,0,0,230,231,5,109,0,0,231,232,5,
        112,0,0,232,233,5,111,0,0,233,234,5,114,0,0,234,235,5,116,0,0,235,
        14,1,0,0,0,236,237,5,102,0,0,237,238,5,114,0,0,238,239,5,111,0,0,
        239,240,5,109,0,0,240,16,1,0,0,0,241,242,5,99,0,0,242,243,5,111,
        0,0,243,244,5,110,0,0,244,245,5,115,0,0,245,246,5,116,0,0,246,18,
        1,0,0,0,247,248,5,97,0,0,248,249,5,115,0,0,249,20,1,0,0,0,250,251,
        5,115,0,0,251,252,5,119,0,0,252,253,5,105,0,0,253,254,5,116,0,0,
        254,255,5,99,0,0,255,256,5,104,0,0,256,22,1,0,0,0,257,258,5,99,0,
        0,258,259,5,97,0,0,259,260,5,115,0,0,260,261,5,101,0,0,261,24,1,
        0,0,0,262,263,5,100,0,0,263,264,5,101,0,0,264,265,5,102,0,0,265,
        266,5,97,0,0,266,267,5,117,0,0,267,268,5,108,0,0,268,269,5,116,0,
        0,269,26,1,0,0,0,270,271,5,98,0,0,271,272,5,114,0,0,272,273,5,101,
        0,0,273,274,5,97,0,0,274,275,5,107,0,0,275,28,1,0,0,0,276,277,5,
        99,0,0,277,278,5,111,0,0,278,279,5,110,0,0,279,280,5,116,0,0,280,
        281,5,105,0,0,281,282,5,110,0,0,282,283,5,117,0,0,283,284,5,101,
        0,0,284,30,1,0,0,0,285,286,5,100,0,0,286,287,5,111,0,0,287,32,1,
        0,0,0,288,289,5,119,0,0,289,290,5,104,0,0,290,291,5,105,0,0,291,
        292,5,108,0,0,292,293,5,101,0,0,293,34,1,0,0,0,294,295,5,105,0,0,
        295,296,5,102,0,0,296,36,1,0,0,0,297,298,5,101,0,0,298,299,5,108,
        0,0,299,300,5,115,0,0,300,301,5,101,0,0,301,38,1,0,0,0,302,303,5,
        102,0,0,303,304,5,111,0,0,304,305,5,114,0,0,305,40,1,0,0,0,306,307,
        5,101,0,0,307,308,5,110,0,0,308,309,5,117,0,0,309,310,5,109,0,0,
        310,42,1,0,0,0,311,312,5,114,0,0,312,313,5,101,0,0,313,314,5,116,
        0,0,314,315,5,117,0,0,315,316,5,114,0,0,316,317,5,110,0,0,317,44,
        1,0,0,0,318,319,5,110,0,0,319,320,5,111,0,0,320,321,5,114,0,0,321,
        322,5,101,0,0,322,323,5,116,0,0,323,46,1,0,0,0,324,325,5,101,0,0,
        325,326,5,110,0,0,326,327,5,116,0,0,327,328,5,114,0,0,328,329,5,
        121,0,0,329,48,1,0,0,0,330,331,5,110,0,0,331,332,5,101,0,0,332,333,
        5,119,0,0,333,50,1,0,0,0,334,335,5,115,0,0,335,336,5,116,0,0,336,
        337,5,114,0,0,337,338,5,117,0,0,338,339,5,99,0,0,339,340,5,116,0,
        0,340,52,1,0,0,0,341,342,5,99,0,0,342,343,5,108,0,0,343,344,5,97,
        0,0,344,345,5,115,0,0,345,346,5,115,0,0,346,54,1,0,0,0,347,348,5,
        116,0,0,348,349,5,121,0,0,349,350,5,112,0,0,350,351,5,101,0,0,351,
        352,5,111,0,0,352,353,5,102,0,0,353,56,1,0,0,0,354,355,5,100,0,0,
        355,356,5,101,0,0,356,357,5,108,0,0,357,358,5,101,0,0,358,359,5,
        116,0,0,359,360,5,101,0,0,360,58,1,0,0,0,361,362,5,40,0,0,362,60,
        1,0,0,0,363,364,5,41,0,0,364,62,1,0,0,0,365,366,5,91,0,0,366,64,
        1,0,0,0,367,368,5,93,0,0,368,66,1,0,0,0,369,370,5,123,0,0,370,68,
        1,0,0,0,371,372,5,125,0,0,372,70,1,0,0,0,373,374,5,43,0,0,374,72,
        1,0,0,0,375,376,5,43,0,0,376,377,5,43,0,0,377,74,1,0,0,0,378,379,
        5,45,0,0,379,76,1,0,0,0,380,381,5,45,0,0,381,382,5,45,0,0,382,78,
        1,0,0,0,383,384,5,42,0,0,384,80,1,0,0,0,385,386,5,47,0,0,386,82,
        1,0,0,0,387,388,5,37,0,0,388,84,1,0,0,0,389,390,5,42,0,0,390,391,
        5,42,0,0,391,86,1,0,0,0,392,393,5,38,0,0,393,394,5,38,0,0,394,88,
        1,0,0,0,395,396,5,124,0,0,396,397,5,124,0,0,397,90,1,0,0,0,398,399,
        5,33,0,0,399,92,1,0,0,0,400,401,5,44,0,0,401,94,1,0,0,0,402,403,
        5,61,0,0,403,96,1,0,0,0,404,405,5,42,0,0,405,406,5,61,0,0,406,98,
        1,0,0,0,407,408,5,47,0,0,408,409,5,61,0,0,409,100,1,0,0,0,410,411,
        5,37,0,0,411,412,5,61,0,0,412,102,1,0,0,0,413,414,5,43,0,0,414,415,
        5,61,0,0,415,104,1,0,0,0,416,417,5,45,0,0,417,418,5,61,0,0,418,106,
        1,0,0,0,419,420,5,61,0,0,420,421,5,61,0,0,421,108,1,0,0,0,422,423,
        5,33,0,0,423,424,5,61,0,0,424,110,1,0,0,0,425,426,5,60,0,0,426,112,
        1,0,0,0,427,428,5,60,0,0,428,429,5,61,0,0,429,114,1,0,0,0,430,431,
        5,62,0,0,431,116,1,0,0,0,432,433,5,62,0,0,433,434,5,61,0,0,434,118,
        1,0,0,0,435,436,5,46,0,0,436,120,1,0,0,0,437,442,3,125,62,0,438,
        441,3,125,62,0,439,441,3,129,64,0,440,438,1,0,0,0,440,439,1,0,0,
        0,441,444,1,0,0,0,442,440,1,0,0,0,442,443,1,0,0,0,443,122,1,0,0,
        0,444,442,1,0,0,0,445,449,5,123,0,0,446,448,7,0,0,0,447,446,1,0,
        0,0,448,451,1,0,0,0,449,447,1,0,0,0,449,450,1,0,0,0,450,452,1,0,
        0,0,451,449,1,0,0,0,452,453,5,125,0,0,453,124,1,0,0,0,454,457,3,
        127,63,0,455,457,3,131,65,0,456,454,1,0,0,0,456,455,1,0,0,0,457,
        126,1,0,0,0,458,459,7,1,0,0,459,128,1,0,0,0,460,461,7,2,0,0,461,
        130,1,0,0,0,462,463,5,92,0,0,463,464,5,117,0,0,464,465,1,0,0,0,465,
        473,3,133,66,0,466,467,5,92,0,0,467,468,5,85,0,0,468,469,1,0,0,0,
        469,470,3,133,66,0,470,471,3,133,66,0,471,473,1,0,0,0,472,462,1,
        0,0,0,472,466,1,0,0,0,473,132,1,0,0,0,474,475,3,151,75,0,475,476,
        3,151,75,0,476,477,3,151,75,0,477,478,3,151,75,0,478,134,1,0,0,0,
        479,481,3,139,69,0,480,482,3,153,76,0,481,480,1,0,0,0,481,482,1,
        0,0,0,482,493,1,0,0,0,483,485,3,141,70,0,484,486,3,153,76,0,485,
        484,1,0,0,0,485,486,1,0,0,0,486,493,1,0,0,0,487,489,3,143,71,0,488,
        490,3,153,76,0,489,488,1,0,0,0,489,490,1,0,0,0,490,493,1,0,0,0,491,
        493,3,137,68,0,492,479,1,0,0,0,492,483,1,0,0,0,492,487,1,0,0,0,492,
        491,1,0,0,0,493,136,1,0,0,0,494,495,5,48,0,0,495,497,7,3,0,0,496,
        498,7,4,0,0,497,496,1,0,0,0,498,499,1,0,0,0,499,497,1,0,0,0,499,
        500,1,0,0,0,500,138,1,0,0,0,501,505,3,147,73,0,502,504,3,129,64,
        0,503,502,1,0,0,0,504,507,1,0,0,0,505,503,1,0,0,0,505,506,1,0,0,
        0,506,140,1,0,0,0,507,505,1,0,0,0,508,512,5,48,0,0,509,511,3,149,
        74,0,510,509,1,0,0,0,511,514,1,0,0,0,512,510,1,0,0,0,512,513,1,0,
        0,0,513,142,1,0,0,0,514,512,1,0,0,0,515,517,3,145,72,0,516,518,3,
        151,75,0,517,516,1,0,0,0,518,519,1,0,0,0,519,517,1,0,0,0,519,520,
        1,0,0,0,520,144,1,0,0,0,521,522,5,48,0,0,522,523,7,5,0,0,523,146,
        1,0,0,0,524,525,7,6,0,0,525,148,1,0,0,0,526,527,7,7,0,0,527,150,
        1,0,0,0,528,529,7,8,0,0,529,152,1,0,0,0,530,532,3,155,77,0,531,533,
        3,157,78,0,532,531,1,0,0,0,532,533,1,0,0,0,533,546,1,0,0,0,534,535,
        3,155,77,0,535,536,3,159,79,0,536,546,1,0,0,0,537,539,3,157,78,0,
        538,540,3,155,77,0,539,538,1,0,0,0,539,540,1,0,0,0,540,546,1,0,0,
        0,541,543,3,159,79,0,542,544,3,155,77,0,543,542,1,0,0,0,543,544,
        1,0,0,0,544,546,1,0,0,0,545,530,1,0,0,0,545,534,1,0,0,0,545,537,
        1,0,0,0,545,541,1,0,0,0,546,154,1,0,0,0,547,548,7,9,0,0,548,156,
        1,0,0,0,549,550,7,10,0,0,550,158,1,0,0,0,551,552,5,108,0,0,552,556,
        5,108,0,0,553,554,5,76,0,0,554,556,5,76,0,0,555,551,1,0,0,0,555,
        553,1,0,0,0,556,160,1,0,0,0,557,560,3,163,81,0,558,560,3,165,82,
        0,559,557,1,0,0,0,559,558,1,0,0,0,560,162,1,0,0,0,561,563,3,167,
        83,0,562,564,3,169,84,0,563,562,1,0,0,0,563,564,1,0,0,0,564,566,
        1,0,0,0,565,567,3,181,90,0,566,565,1,0,0,0,566,567,1,0,0,0,567,574,
        1,0,0,0,568,569,3,173,86,0,569,571,3,169,84,0,570,572,3,181,90,0,
        571,570,1,0,0,0,571,572,1,0,0,0,572,574,1,0,0,0,573,561,1,0,0,0,
        573,568,1,0,0,0,574,164,1,0,0,0,575,578,3,145,72,0,576,579,3,175,
        87,0,577,579,3,179,89,0,578,576,1,0,0,0,578,577,1,0,0,0,579,580,
        1,0,0,0,580,582,3,177,88,0,581,583,3,181,90,0,582,581,1,0,0,0,582,
        583,1,0,0,0,583,166,1,0,0,0,584,586,3,173,86,0,585,584,1,0,0,0,585,
        586,1,0,0,0,586,587,1,0,0,0,587,588,5,46,0,0,588,593,3,173,86,0,
        589,590,3,173,86,0,590,591,5,46,0,0,591,593,1,0,0,0,592,585,1,0,
        0,0,592,589,1,0,0,0,593,168,1,0,0,0,594,596,7,11,0,0,595,597,3,171,
        85,0,596,595,1,0,0,0,596,597,1,0,0,0,597,598,1,0,0,0,598,599,3,173,
        86,0,599,170,1,0,0,0,600,601,7,12,0,0,601,172,1,0,0,0,602,604,3,
        129,64,0,603,602,1,0,0,0,604,605,1,0,0,0,605,603,1,0,0,0,605,606,
        1,0,0,0,606,174,1,0,0,0,607,609,3,179,89,0,608,607,1,0,0,0,608,609,
        1,0,0,0,609,610,1,0,0,0,610,611,5,46,0,0,611,616,3,179,89,0,612,
        613,3,179,89,0,613,614,5,46,0,0,614,616,1,0,0,0,615,608,1,0,0,0,
        615,612,1,0,0,0,616,176,1,0,0,0,617,619,7,13,0,0,618,620,3,171,85,
        0,619,618,1,0,0,0,619,620,1,0,0,0,620,621,1,0,0,0,621,622,3,173,
        86,0,622,178,1,0,0,0,623,625,3,151,75,0,624,623,1,0,0,0,625,626,
        1,0,0,0,626,624,1,0,0,0,626,627,1,0,0,0,627,180,1,0,0,0,628,629,
        7,14,0,0,629,182,1,0,0,0,630,631,5,39,0,0,631,632,3,185,92,0,632,
        633,5,39,0,0,633,184,1,0,0,0,634,636,3,187,93,0,635,634,1,0,0,0,
        636,637,1,0,0,0,637,635,1,0,0,0,637,638,1,0,0,0,638,186,1,0,0,0,
        639,642,8,15,0,0,640,642,3,189,94,0,641,639,1,0,0,0,641,640,1,0,
        0,0,642,188,1,0,0,0,643,648,3,191,95,0,644,648,3,193,96,0,645,648,
        3,195,97,0,646,648,3,131,65,0,647,643,1,0,0,0,647,644,1,0,0,0,647,
        645,1,0,0,0,647,646,1,0,0,0,648,190,1,0,0,0,649,650,5,92,0,0,650,
        651,7,16,0,0,651,192,1,0,0,0,652,653,5,92,0,0,653,655,3,149,74,0,
        654,656,3,149,74,0,655,654,1,0,0,0,655,656,1,0,0,0,656,658,1,0,0,
        0,657,659,3,149,74,0,658,657,1,0,0,0,658,659,1,0,0,0,659,194,1,0,
        0,0,660,661,5,92,0,0,661,662,5,120,0,0,662,664,1,0,0,0,663,665,3,
        151,75,0,664,663,1,0,0,0,665,666,1,0,0,0,666,664,1,0,0,0,666,667,
        1,0,0,0,667,196,1,0,0,0,668,669,5,102,0,0,669,671,5,34,0,0,670,672,
        3,201,100,0,671,670,1,0,0,0,671,672,1,0,0,0,672,673,1,0,0,0,673,
        674,5,34,0,0,674,198,1,0,0,0,675,677,5,34,0,0,676,678,3,201,100,
        0,677,676,1,0,0,0,677,678,1,0,0,0,678,679,1,0,0,0,679,680,5,34,0,
        0,680,200,1,0,0,0,681,683,3,203,101,0,682,681,1,0,0,0,683,684,1,
        0,0,0,684,682,1,0,0,0,684,685,1,0,0,0,685,202,1,0,0,0,686,694,8,
        17,0,0,687,694,3,189,94,0,688,689,5,92,0,0,689,694,5,10,0,0,690,
        691,5,92,0,0,691,692,5,13,0,0,692,694,5,10,0,0,693,686,1,0,0,0,693,
        687,1,0,0,0,693,688,1,0,0,0,693,690,1,0,0,0,694,204,1,0,0,0,695,
        697,7,18,0,0,696,695,1,0,0,0,697,698,1,0,0,0,698,696,1,0,0,0,698,
        699,1,0,0,0,699,700,1,0,0,0,700,701,6,102,0,0,701,206,1,0,0,0,702,
        703,5,47,0,0,703,704,5,42,0,0,704,708,1,0,0,0,705,707,9,0,0,0,706,
        705,1,0,0,0,707,710,1,0,0,0,708,709,1,0,0,0,708,706,1,0,0,0,709,
        711,1,0,0,0,710,708,1,0,0,0,711,712,5,42,0,0,712,713,5,47,0,0,713,
        714,1,0,0,0,714,715,6,103,0,0,715,208,1,0,0,0,716,718,5,13,0,0,717,
        719,5,10,0,0,718,717,1,0,0,0,718,719,1,0,0,0,719,722,1,0,0,0,720,
        722,5,10,0,0,721,716,1,0,0,0,721,720,1,0,0,0,722,723,1,0,0,0,723,
        724,6,104,0,0,724,210,1,0,0,0,48,0,440,442,449,456,472,481,485,489,
        492,499,505,512,519,532,539,543,545,555,559,563,566,571,573,578,
        582,585,592,596,605,608,615,619,626,637,641,647,655,658,666,671,
        677,684,693,698,708,718,721,1,6,0,0
    ]

class ParaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    Import = 7
    From = 8
    Const = 9
    As = 10
    Switch = 11
    Case = 12
    Default = 13
    Break = 14
    Continue = 15
    Do = 16
    While = 17
    If = 18
    Else = 19
    For = 20
    Enum = 21
    Return = 22
    NoRet = 23
    Entry = 24
    New = 25
    Struct = 26
    Class = 27
    Typeof = 28
    Delete = 29
    LeftParen = 30
    RightParen = 31
    LeftBracket = 32
    RightBracket = 33
    LeftBrace = 34
    RightBrace = 35
    Plus = 36
    PlusPlus = 37
    Minus = 38
    MinusMinus = 39
    Star = 40
    Div = 41
    Mod = 42
    PowerTo = 43
    AndAnd = 44
    OrOr = 45
    Not = 46
    Comma = 47
    Assign = 48
    StarAssign = 49
    DivAssign = 50
    ModAssign = 51
    PlusAssign = 52
    MinusAssign = 53
    Equal = 54
    NotEqual = 55
    Less = 56
    LessEqual = 57
    Greater = 58
    GreaterEqual = 59
    Dot = 60
    Identifier = 61
    IntegerConstant = 62
    FloatingConstant = 63
    DigitSequence = 64
    CharacterConstant = 65
    FStringLiteral = 66
    StringLiteral = 67
    Whitespace = 68
    BlockComment = 69
    Newline = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'=>'", "'init'", "';'", "'?'", "':'", "'...'", "'import'", 
            "'from'", "'const'", "'as'", "'switch'", "'case'", "'default'", 
            "'break'", "'continue'", "'do'", "'while'", "'if'", "'else'", 
            "'for'", "'enum'", "'return'", "'noret'", "'entry'", "'new'", 
            "'struct'", "'class'", "'typeof'", "'delete'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'+'", "'++'", "'-'", "'--'", "'*'", 
            "'/'", "'%'", "'**'", "'&&'", "'||'", "'!'", "','", "'='", "'*='", 
            "'/='", "'%='", "'+='", "'-='", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "Import", "From", "Const", "As", "Switch", "Case", "Default", 
            "Break", "Continue", "Do", "While", "If", "Else", "For", "Enum", 
            "Return", "NoRet", "Entry", "New", "Struct", "Class", "Typeof", 
            "Delete", "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
            "LeftBrace", "RightBrace", "Plus", "PlusPlus", "Minus", "MinusMinus", 
            "Star", "Div", "Mod", "PowerTo", "AndAnd", "OrOr", "Not", "Comma", 
            "Assign", "StarAssign", "DivAssign", "ModAssign", "PlusAssign", 
            "MinusAssign", "Equal", "NotEqual", "Less", "LessEqual", "Greater", 
            "GreaterEqual", "Dot", "Identifier", "IntegerConstant", "FloatingConstant", 
            "DigitSequence", "CharacterConstant", "FStringLiteral", "StringLiteral", 
            "Whitespace", "BlockComment", "Newline" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "Import", 
                  "From", "Const", "As", "Switch", "Case", "Default", "Break", 
                  "Continue", "Do", "While", "If", "Else", "For", "Enum", 
                  "Return", "NoRet", "Entry", "New", "Struct", "Class", 
                  "Typeof", "Delete", "LeftParen", "RightParen", "LeftBracket", 
                  "RightBracket", "LeftBrace", "RightBrace", "Plus", "PlusPlus", 
                  "Minus", "MinusMinus", "Star", "Div", "Mod", "PowerTo", 
                  "AndAnd", "OrOr", "Not", "Comma", "Assign", "StarAssign", 
                  "DivAssign", "ModAssign", "PlusAssign", "MinusAssign", 
                  "Equal", "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual", 
                  "Dot", "Identifier", "ExtensionTaskBlock", "IdentifierNondigit", 
                  "Nondigit", "Digit", "UniversalCharacterName", "HexQuad", 
                  "IntegerConstant", "BinaryConstant", "DecimalConstant", 
                  "OctalConstant", "HexadecimalConstant", "HexadecimalPrefix", 
                  "NonzeroDigit", "OctalDigit", "HexadecimalDigit", "IntegerSuffix", 
                  "UnsignedSuffix", "LongSuffix", "LongLongSuffix", "FloatingConstant", 
                  "DecimalFloatingConstant", "HexadecimalFloatingConstant", 
                  "FractionalConstant", "ExponentPart", "Sign", "DigitSequence", 
                  "HexadecimalFractionalConstant", "BinaryExponentPart", 
                  "HexadecimalDigitSequence", "FloatingSuffix", "CharacterConstant", 
                  "CCharSequence", "CChar", "EscapeSequence", "SimpleEscapeSequence", 
                  "OctalEscapeSequence", "HexadecimalEscapeSequence", "FStringLiteral", 
                  "StringLiteral", "SCharSequence", "SChar", "Whitespace", 
                  "BlockComment", "Newline" ]

    grammarFileName = "Para.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


