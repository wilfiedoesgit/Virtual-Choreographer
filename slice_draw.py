import numpy as np
import cv2
from BT import *
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import argparse
import csv

order = [[[(790, 663), (820, 693)], [(790, 664), (820, 693)], [(790, 664), (820, 693)], [(791, 663), (820, 693)], [(790, 663), (820, 692)], [(791, 663), (820, 693)], [(791, 666), (820, 694)], [(790, 665), (820, 693)], [(790, 664), (820, 693)], [(790, 663), (820, 693)], [(790, 663), (820, 693)], [(790, 663), (820, 693)], [(791, 664), (820, 693)], [(792, 663), (820, 693)], [(792, 663), (820, 691)], [(791, 662), (820, 690)], [(789, 661), (816, 689)], [(781, 662), (809, 689)], [(771, 664), (801, 691)], [(758, 668), (790, 697)], [(754, 670), (785, 699)], [(752, 670), (783, 700)], [(750, 670), (781, 701)], [(748, 671), (778, 700)], [(748, 671), (779, 700)], [(749, 671), (779, 700)], [(750, 671), (780, 700)], [(751, 672), (780, 701)], [(751, 671), (780, 700)], [(751, 671), (782, 700)], [(752, 672), (782, 701)], [(753, 672), (783, 701)], [(754, 672), (784, 701)], [(754, 672), (784, 701)], [(755, 672), (786, 701)], [(757, 673), (788, 701)], [(761, 673), (791, 700)], [(767, 671), (797, 699)], [(775, 672), (805, 701)], [(785, 674), (816, 704)], [(794, 677), (825, 708)], [(801, 681), (832, 711)], [(806, 683), (838, 714)], [(809, 687), (841, 718)], [(810, 688), (842, 719)], [(809, 687), (842, 720)], [(808, 688), (840, 720)], [(806, 688), (838, 720)], [(806, 688), (838, 720)], [(806, 688), (838, 720)], [(807, 689), (839, 720)], [(807, 688), (839, 720)], [(807, 688), (840, 720)], [(808, 689), (841, 720)], [(808, 689), (841, 720)], [(808, 691), (841, 720)], [(808, 691), (842, 720)], [(808, 691), (842, 720)], [(808, 688), (842, 720)], [(809, 686), (842, 720)], [(806, 681), (840, 714)], [(796, 671), (833, 707)], [(778, 662), (814, 693)], [(754, 652), (787, 679)], [(727, 643), (758, 667)], [(703, 637), (728, 655)], [(622, 619), (643, 639)], [(711, 619), (740, 636)], [(738, 628), (774, 652)], [(776, 638), (809, 664)], [(797, 644), (830, 675)], [(814, 649), (845, 681)], [(817, 655), (847, 686)], [(818, 659), (850, 689)], [(819, 662), (851, 692)], [(822, 664), (853, 694)], [(822, 664), (854, 695)], [(822, 664), (854, 695)], [(823, 665), (854, 695)], [(823, 665), (854, 695)], [(823, 666), (854, 695)], [(823, 666), (854, 694)], [(823, 665), (854, 694)], [(823, 666), (854, 695)], [(823, 664), (854, 694)], [(823, 665), (854, 695)], [(824, 665), (854, 695)], [(824, 665), (855, 695)], [(824, 665), (855, 695)], [(824, 666), (855, 696)], [(825, 665), (856, 695)], [(826, 666), (857, 696)], [(827, 669), (858, 697)], [(828, 668), (859, 697)], [(828, 667), (860, 697)], [(828, 668), (860, 697)], [(827, 668), (860, 697)], [(826, 667), (859, 697)], [(824, 666), (858, 696)], [(824, 666), (857, 696)], [(825, 666), (857, 695)], [(825, 666), (857, 695)], [(826, 665), (858, 695)], [(826, 665), (858, 695)], [(826, 665), (858, 694)], [(825, 665), (857, 694)], [(825, 665), (857, 694)], [(825, 665), (856, 693)], [(825, 664), (856, 693)], [(825, 664), (856, 693)], [(825, 664), (856, 693)], [(825, 664), (857, 693)], [(825, 664), (857, 693)], [(826, 664), (857, 693)], [(826, 664), (857, 693)], [(826, 663), (858, 693)], [(826, 663), (858, 693)], [(826, 663), (857, 693)], [(826, 664), (857, 693)], [(825, 663), (857, 694)], [(825, 664), (857, 694)], [(826, 664), (857, 694)], [(826, 664), (857, 695)], [(826, 664), (858, 695)], [(826, 664), (858, 695)], [(827, 664), (858, 694)], [(827, 664), (858, 694)], [(827, 664), (858, 695)], [(825, 664), (858, 694)], [(825, 664), (857, 694)], [(825, 664), (857, 693)], [(825, 664), (857, 695)], [(825, 664), (857, 695)], [(826, 664), (857, 695)], [(826, 664), (857, 695)], [(826, 664), (857, 694)], [(826, 664), (857, 694)], [(826, 664), (857, 694)], [(825, 664), (857, 694)], [(825, 664), (857, 694)], [(825, 664), (857, 693)], [(825, 664), (857, 695)], [(826, 664), (857, 695)], [(825, 664), (857, 695)], [(825, 664), (858, 694)], [(825, 664), (858, 695)], [(825, 664), (858, 694)], [(826, 664), (858, 694)], [(826, 664), (858, 694)], [(826, 664), (858, 694)], [(826, 664), (859, 694)], [(827, 664), (859, 694)], [(828, 664), (860, 694)], [(826, 664), (861, 694)], [(826, 663), (861, 694)], [(826, 663), (861, 693)], [(825, 663), (860, 694)], [(824, 663), (859, 694)], [(822, 664), (857, 693)], [(819, 662), (851, 691)], [(811, 662), (844, 691)], [(799, 663), (833, 691)], [(786, 664), (821, 691)], [(773, 664), (806, 692)], [(759, 664), (793, 693)], [(747, 664), (779, 692)], [(737, 665), (770, 693)], [(729, 667), (763, 696)], [(728, 668), (761, 697)], [(728, 668), (761, 698)], [(729, 668), (762, 698)], [(729, 669), (762, 704)], [(729, 669), (762, 704)], [(729, 669), (762, 705)], [(729, 670), (762, 705)], [(728, 671), (763, 701)], [(727, 674), (760, 704)], [(725, 676), (760, 706)], [(725, 668), (757, 702)], [(720, 657), (754, 689)], [(713, 648), (746, 678)], [(697, 641), (735, 671)], [(687, 638), (725, 668)], [(680, 638), (717, 668)], [(674, 642), (711, 672)], [(669, 648), (705, 679)], [(667, 656), (704, 686)], [(669, 664), (704, 694)], [(671, 669), (706, 701)], [(674, 674), (708, 707)], [(677, 679), (713, 711)], [(682, 683), (717, 715)], [(686, 687), (721, 720)], [(689, 689), (724, 720)], [(690, 690), (725, 720)], [(690, 689), (725, 720)], [(690, 689), (725, 720)], [(690, 690), (725, 720)], [(690, 690), (725, 720)], [(690, 690), (725, 720)], [(691, 690), (725, 720)], [(691, 690), (725, 720)], [(691, 690), (726, 720)], [(691, 690), (726, 720)], [(690, 690), (726, 720)], [(690, 690), (725, 720)], [(690, 689), (725, 720)], [(689, 689), (724, 720)], [(689, 689), (724, 720)], [(689, 689), (724, 720)], [(689, 689), (724, 720)], [(689, 689), (725, 720)], [(691, 689), (726, 720)], [(692, 689), (727, 720)], [(693, 689), (728, 720)], [(694, 689), (729, 720)], [(694, 689), (729, 720)], [(695, 689), (729, 720)], [(694, 688), (729, 720)], [(694, 688), (729, 720)], [(694, 688), (729, 720)], [(693, 689), (728, 720)], [(692, 688), (727, 720)], [(691, 688), (726, 720)], [(690, 688), (725, 720)], [(690, 688), (724, 720)], [(690, 689), (724, 720)], [(689, 688), (724, 720)], [(689, 688), (724, 720)], [(690, 689), (724, 720)], [(689, 689), (724, 720)], [(688, 688), (723, 720)], [(688, 688), (723, 720)], [(688, 688), (722, 720)], [(688, 688), (722, 720)], [(688, 688), (723, 720)], [(689, 688), (723, 720)], [(690, 689), (724, 720)], [(690, 689), (725, 720)], [(691, 689), (725, 720)], [(691, 689), (726, 720)], [(693, 690), (727, 720)], [(695, 690), (729, 720)], [(696, 689), (730, 720)], [(698, 689), (732, 720)], [(703, 688), (737, 720)], [(716, 685), (749, 714)], [(729, 678), (758, 711)], [(732, 679), (760, 711)], [(734, 679), (761, 712)], [(734, 681), (761, 713)], [(734, 680), (762, 713)], [(734, 681), (763, 713)], [(735, 680), (764, 713)], [(735, 681), (766, 712)], [(736, 681), (768, 710)], [(738, 680), (769, 711)], [(740, 680), (772, 710)], [(742, 680), (775, 710)], [(745, 681), (777, 711)], [(748, 682), (781, 713)], [(749, 683), (783, 713)], [(750, 684), (784, 715)], [(751, 686), (785, 716)], [(751, 686), (785, 717)], [(751, 686), (786, 715)], [(752, 686), (786, 716)], [(755, 686), (787, 715)], [(756, 685), (787, 715)], [(754, 684), (789, 714)], [(754, 684), (787, 715)], [(753, 683), (786, 715)], [(753, 683), (786, 714)], [(757, 683), (789, 713)], [(759, 683), (794, 714)], [(766, 682), (799, 713)], [(766, 682), (798, 713)], [(765, 683), (801, 714)], [(766, 683), (801, 714)], [(764, 684), (799, 715)], [(766, 685), (797, 716)], [(766, 684), (797, 715)], [(768, 684), (798, 716)], [(771, 685), (801, 716)], [(777, 687), (813, 717)], [(788, 670), (821, 707)], [(798, 653), (833, 690)], [(813, 631), (853, 670)], [(835, 618), (870, 646)], [(864, 591), (894, 619)], [(888, 566), (915, 592)], [(902, 541), (932, 571)], [(910, 527), (945, 558)], [(912, 522), (945, 554)], [(908, 528), (941, 559)], [(898, 550), (929, 578)], [(882, 566), (909, 596)], [(852, 588), (884, 619)], [(825, 611), (856, 642)], [(794, 627), (838, 659)], [(772, 637), (812, 672)], [(750, 650), (787, 683)], [(736, 662), (770, 693)], [(727, 672), (758, 702)], [(724, 671), (754, 701)], [(720, 670), (753, 700)], [(721, 670), (752, 699)], [(721, 670), (753, 700)], [(722, 670), (753, 700)], [(723, 670), (754, 700)], [(724, 670), (755, 700)], [(722, 670), (753, 699)], [(721, 669), (752, 699)], [(720, 669), (750, 699)], [(719, 668), (749, 699)], [(719, 669), (748, 699)], [(719, 668), (749, 700)], [(719, 669), (749, 699)], [(719, 668), (749, 699)], [(719, 669), (749, 699)], [(719, 669), (749, 699)], [(718, 668), (749, 699)], [(718, 668), (749, 699)], [(718, 668), (749, 700)], [(718, 668), (749, 699)], [(718, 669), (749, 699)], [(718, 668), (749, 698)], [(718, 668), (750, 699)], [(718, 668), (750, 699)], [(719, 668), (750, 699)], [(720, 667), (752, 698)], [(722, 666), (753, 697)], [(726, 663), (757, 693)], [(731, 658), (762, 689)], [(737, 651), (767, 682)], [(743, 646), (771, 675)], [(747, 643), (775, 671)], [(749, 641), (777, 670)], [(750, 642), (778, 670)], [(749, 642), (777, 669)], [(746, 641), (774, 670)], [(746, 641), (774, 670)], [(746, 641), (775, 669)], [(746, 641), (776, 669)], [(746, 641), (775, 669)], [(746, 641), (775, 669)]], [[(550, 118), (582, 132)], [(678, 121), (706, 141)], [(677, 116), (707, 136)], [(541, 10), (570, 31)], [(534, 0), (569, 15)], [(538, 0), (574, 28)], [(549, 27), (574, 48)], [(572, 177), (616, 203)], [(577, 175), (616, 201)], [(556, 91), (584, 108)], [(530, 86), (562, 107)], [(509, 99), (538, 116)], [(365, 141), (397, 161)], [(346, 138), (382, 156)], [(334, 87), (370, 107)], [(326, 66), (362, 89)], [(308, 49), (350, 70)], [(302, 44), (349, 69)], [(328, 65), (361, 81)]], [[(909, 143), (943, 165)], [(877, 152), (911, 180)], [(846, 174), (885, 204)], [(813, 205), (844, 233)], [(788, 238), (814, 269)], [(750, 318), (771, 345)], [(740, 348), (766, 373)], [(737, 374), (762, 396)], [(737, 391), (763, 415)], [(741, 407), (767, 428)], [(748, 417), (773, 438)], [(762, 426), (786, 444)], [(809, 420), (837, 437)], [(834, 413), (861, 430)], [(935, 322), (959, 341)], [(926, 324), (950, 344)], [(910, 329), (937, 349)], [(893, 336), (919, 358)], [(878, 347), (902, 369)], [(866, 358), (891, 380)], [(866, 358), (891, 380)], [(857, 372), (881, 391)], [(849, 385), (873, 404)], [(843, 391), (866, 413)], [(811, 314), (835, 332)], [(796, 315), (821, 332)], [(783, 314), (806, 333)], [(770, 319), (796, 336)], [(759, 325), (785, 343)], [(751, 334), (775, 355)], [(730, 359), (754, 377)], [(717, 365), (742, 382)], [(705, 361), (730, 379)], [(696, 354), (720, 371)], [(679, 342), (702, 359)], [(665, 393), (687, 414)], [(667, 395), (690, 417)], [(665, 393), (688, 412)], [(651, 371), (674, 389)], [(648, 366), (673, 384)], [(649, 366), (676, 383)], [(654, 369), (680, 386)], [(659, 373), (684, 391)], [(660, 374), (686, 392)], [(664, 371), (689, 390)], [(673, 368), (698, 387)], [(681, 367), (706, 385)], [(690, 367), (714, 384)], [(702, 365), (726, 382)], [(713, 361), (737, 379)], [(722, 357), (747, 375)], [(731, 354), (755, 372)], [(739, 355), (764, 373)], [(749, 357), (775, 375)], [(782, 259), (808, 280)], [(779, 244), (805, 267)], [(781, 24), (805, 53)], [(780, 2), (808, 30)], [(788, 0), (818, 18)], [(791, 12), (815, 43)], [(787, 40), (813, 72)], [(779, 70), (809, 102)], [(776, 94), (808, 124)], [(769, 113), (803, 139)], [(767, 119), (800, 145)], [(760, 119), (795, 143)], [(750, 123), (785, 151)], [(733, 146), (761, 182)], [(718, 195), (738, 226)], [(703, 228), (730, 253)], [(687, 232), (716, 254)], [(629, 118), (656, 142)], [(614, 111), (642, 131)], [(596, 109), (626, 132)], [(585, 108), (616, 130)], [(585, 111), (615, 136)], [(600, 123), (628, 156)], [(629, 156), (651, 178)], [(660, 184), (685, 209)], [(673, 200), (701, 221)], [(673, 199), (701, 220)], [(686, 204), (707, 224)], [(701, 211), (726, 230)], [(717, 210), (743, 229)], [(734, 199), (761, 220)], [(752, 178), (775, 201)], [(767, 155), (792, 179)], [(773, 145), (802, 168)], [(773, 142), (803, 165)], [(771, 145), (800, 169)], [(766, 154), (793, 185)], [(753, 179), (786, 207)], [(743, 198), (771, 220)], [(742, 202), (770, 223)], [(747, 199), (777, 221)], [(756, 192), (784, 214)], [(768, 179), (794, 203)], [(778, 167), (809, 191)], [(788, 161), (820, 183)], [(796, 155), (828, 179)], [(811, 156), (842, 182)], [(821, 174), (847, 202)], [(823, 206), (845, 233)], [(814, 246), (837, 266)], [(795, 287), (821, 307)], [(795, 297), (823, 316)], [(800, 299), (826, 319)], [(802, 297), (829, 317)], [(808, 292), (834, 313)], [(816, 285), (842, 306)], [(826, 277), (853, 298)], [(840, 267), (866, 287)], [(854, 259), (879, 277)], [(879, 233), (907, 253)], [(883, 232), (913, 253)], [(882, 235), (911, 255)], [(881, 243), (905, 263)], [(870, 262), (893, 284)], [(828, 391), (851, 413)], [(827, 392), (850, 414)], [(894, 282), (914, 306)], [(904, 266), (925, 289)], [(916, 254), (937, 275)], [(928, 246), (952, 265)], [(940, 238), (962, 258)], [(946, 234), (971, 254)], [(952, 235), (977, 253)], [(957, 238), (981, 257)], [(961, 244), (985, 261)], [(963, 248), (986, 267)], [(943, 299), (964, 321)], [(904, 349), (927, 367)], [(888, 364), (914, 382)], [(882, 371), (907, 390)], [(868, 388), (891, 407)], [(856, 393), (883, 412)], [(850, 394), (877, 413)], [(848, 391), (876, 410)], [(851, 387), (878, 405)], [(860, 381), (883, 400)], [(886, 358), (912, 378)], [(902, 348), (928, 365)], [(916, 332), (943, 352)], [(931, 315), (954, 338)], [(937, 303), (962, 327)], [(937, 298), (964, 318)], [(924, 292), (954, 312)], [(606, 146), (648, 170)], [(557, 124), (604, 149)], [(520, 112), (562, 133)], [(492, 108), (531, 130)], [(478, 109), (514, 133)], [(471, 116), (499, 142)], [(471, 132), (497, 157)], [(476, 150), (501, 172)], [(465, 202), (491, 220)], [(484, 205), (517, 225)], [(511, 212), (549, 238)], [(550, 230), (579, 253)], [(571, 247), (598, 269)], [(576, 255), (612, 275)], [(582, 250), (606, 267)], [(587, 234), (610, 255)], [(594, 211), (616, 236)], [(601, 185), (623, 212)], [(605, 155), (629, 185)], [(606, 130), (631, 159)], [(605, 104), (633, 135)], [(601, 84), (635, 113)], [(597, 69), (629, 98)], [(593, 56), (628, 83)], [(586, 50), (620, 76)], [(578, 50), (613, 75)], [(571, 52), (604, 77)], [(561, 59), (594, 83)], [(551, 70), (586, 102)], [(547, 91), (579, 117)], [(544, 111), (573, 140)], [(542, 137), (566, 169)], [(543, 168), (567, 200)], [(549, 200), (573, 231)], [(559, 228), (586, 254)], [(573, 237), (601, 258)], [(586, 218), (611, 242)], [(598, 182), (623, 213)], [(603, 156), (633, 187)], [(603, 138), (635, 166)], [(599, 135), (632, 160)], [(598, 144), (629, 174)], [(603, 170), (630, 202)], [(604, 204), (627, 238)], [(601, 238), (627, 269)], [(598, 258), (631, 284)], [(598, 253), (627, 280)], [(597, 224), (621, 255)], [(592, 181), (613, 218)], [(587, 132), (603, 172)], [(587, 87), (610, 130)], [(595, 64), (628, 96)], [(603, 54), (639, 79)], [(616, 56), (649, 84)], [(628, 74), (652, 107)], [(624, 104), (650, 140)], [(618, 142), (648, 177)], [(612, 171), (641, 200)], [(600, 189), (629, 209)], [(594, 182), (621, 205)], [(594, 158), (619, 190)], [(601, 128), (623, 162)], [(606, 100), (633, 134)], [(616, 69), (644, 103)], [(629, 39), (659, 76)], [(650, 12), (682, 42)], [(674, 0), (705, 17)], [(662, 6), (702, 50)], [(640, 47), (672, 89)], [(617, 86), (645, 129)], [(602, 134), (625, 178)], [(590, 325), (612, 350)], [(594, 351), (619, 376)], [(599, 374), (627, 395)], [(609, 384), (637, 405)], [(625, 390), (654, 408)], [(644, 387), (672, 405)], [(663, 379), (689, 398)], [(680, 373), (706, 392)], [(696, 365), (722, 384)], [(711, 357), (737, 376)], [(725, 348), (751, 369)], [(738, 342), (765, 362)], [(751, 337), (778, 357)], [(765, 333), (793, 353)], [(781, 331), (807, 350)], [(795, 327), (824, 347)], [(806, 324), (833, 344)], [(812, 319), (839, 340)], [(813, 317), (841, 337)], [(810, 316), (838, 337)], [(803, 320), (830, 340)], [(793, 326), (820, 345)], [(784, 334), (810, 352)], [(778, 340), (801, 359)], [(770, 346), (794, 365)], [(764, 353), (788, 371)], [(757, 360), (782, 378)], [(753, 366), (778, 383)], [(748, 369), (774, 386)], [(745, 368), (769, 386)], [(741, 363), (767, 381)], [(739, 357), (763, 374)], [(739, 348), (763, 367)], [(741, 342), (766, 361)]], [[(638, 629), (668, 679)], [(633, 634), (664, 683)], [(627, 637), (659, 688)], [(620, 640), (653, 692)], [(608, 646), (643, 696)], [(597, 650), (633, 699)], [(586, 653), (623, 703)], [(576, 655), (613, 706)], [(566, 659), (604, 710)], [(563, 664), (599, 714)], [(561, 665), (596, 714)], [(563, 666), (599, 712)], [(564, 667), (600, 712)], [(564, 669), (600, 712)], [(563, 669), (600, 712)], [(562, 669), (599, 712)], [(563, 670), (600, 713)], [(562, 670), (607, 713)], [(562, 669), (602, 713)], [(562, 668), (601, 712)], [(561, 667), (600, 710)], [(559, 666), (597, 709)], [(553, 662), (593, 706)], [(545, 659), (585, 704)], [(541, 659), (579, 702)], [(539, 658), (578, 702)], [(540, 657), (581, 702)], [(543, 657), (584, 704)], [(552, 659), (590, 708)], [(557, 662), (595, 711)], [(562, 669), (602, 720)], [(567, 675), (607, 720)], [(567, 677), (608, 720)], [(567, 677), (608, 720)], [(567, 678), (609, 720)], [(568, 679), (610, 720)], [(568, 680), (609, 720)], [(568, 680), (609, 720)], [(568, 681), (609, 720)], [(568, 681), (610, 720)], [(568, 681), (610, 720)], [(568, 680), (609, 720)], [(567, 678), (609, 720)], [(566, 677), (609, 720)], [(565, 676), (606, 720)], [(565, 676), (606, 720)], [(566, 675), (606, 720)], [(566, 675), (607, 720)], [(568, 675), (609, 720)], [(568, 673), (610, 720)], [(568, 671), (611, 718)], [(568, 666), (609, 714)], [(567, 659), (607, 709)], [(563, 653), (604, 703)], [(559, 649), (598, 700)], [(552, 648), (592, 699)], [(549, 654), (589, 705)], [(548, 658), (587, 709)], [(548, 659), (588, 707)], [(548, 662), (587, 707)], [(549, 662), (587, 705)], [(548, 662), (587, 705)], [(549, 662), (587, 705)], [(548, 662), (587, 706)], [(547, 660), (585, 706)], [(545, 658), (583, 706)], [(544, 658), (583, 706)], [(545, 657), (578, 705)], [(544, 657), (578, 705)], [(547, 657), (581, 706)], [(548, 658), (583, 705)], [(548, 659), (584, 705)], [(548, 661), (584, 706)], [(547, 659), (582, 706)], [(546, 659), (580, 706)], [(546, 659), (579, 706)], [(544, 658), (578, 706)], [(544, 656), (577, 704)], [(543, 656), (576, 703)], [(544, 657), (578, 704)], [(546, 658), (580, 705)], [(547, 661), (583, 705)], [(548, 661), (585, 705)], [(548, 661), (586, 705)], [(549, 661), (586, 705)], [(549, 662), (587, 705)], [(550, 662), (587, 705)], [(550, 662), (586, 705)], [(551, 661), (586, 704)], [(550, 661), (586, 704)], [(550, 661), (586, 703)], [(550, 661), (586, 703)], [(550, 661), (586, 703)], [(550, 661), (586, 703)], [(550, 661), (586, 703)], [(550, 661), (586, 703)], [(550, 661), (586, 703)], [(550, 660), (586, 703)], [(550, 659), (586, 703)], [(550, 659), (586, 702)], [(550, 658), (586, 701)], [(550, 657), (586, 700)], [(550, 657), (586, 701)], [(550, 657), (586, 701)], [(550, 657), (586, 701)], [(550, 657), (586, 701)], [(550, 658), (585, 702)], [(550, 658), (585, 704)], [(549, 658), (584, 703)], [(549, 659), (584, 703)], [(549, 658), (584, 703)], [(549, 658), (583, 704)], [(549, 658), (583, 704)], [(548, 658), (581, 705)], [(547, 658), (579, 705)], [(546, 658), (577, 705)], [(543, 658), (577, 706)], [(544, 658), (578, 707)], [(542, 658), (578, 707)], [(542, 658), (579, 707)], [(542, 658), (580, 705)], [(542, 659), (581, 705)], [(545, 660), (583, 705)], [(544, 659), (583, 704)], [(544, 660), (583, 704)], [(544, 659), (583, 704)], [(544, 659), (583, 704)], [(544, 659), (583, 704)], [(543, 658), (582, 703)], [(544, 658), (582, 704)], [(544, 658), (582, 703)], [(543, 659), (582, 703)], [(543, 659), (582, 703)], [(543, 659), (582, 703)], [(544, 659), (582, 703)], [(543, 659), (582, 703)], [(544, 659), (583, 703)], [(544, 659), (583, 703)], [(544, 659), (583, 703)], [(544, 659), (582, 703)], [(544, 659), (582, 703)], [(544, 659), (583, 703)], [(543, 658), (582, 703)], [(543, 658), (582, 703)], [(543, 658), (582, 703)], [(543, 658), (582, 704)], [(543, 658), (581, 704)], [(542, 658), (580, 704)], [(542, 658), (579, 704)], [(542, 658), (578, 704)], [(543, 658), (579, 703)], [(542, 658), (580, 703)], [(542, 658), (579, 704)], [(542, 659), (580, 704)], [(542, 659), (580, 704)], [(542, 659), (580, 704)], [(542, 659), (580, 704)], [(542, 659), (580, 704)], [(542, 659), (580, 704)], [(542, 659), (580, 704)], [(542, 660), (580, 704)], [(542, 660), (580, 704)], [(542, 660), (580, 704)], [(542, 660), (580, 704)], [(543, 660), (580, 704)], [(543, 659), (580, 704)], [(543, 660), (581, 704)], [(543, 660), (581, 704)], [(543, 661), (582, 704)], [(543, 661), (582, 704)], [(542, 661), (581, 704)], [(543, 661), (581, 704)], [(543, 661), (580, 704)], [(543, 662), (580, 704)], [(542, 662), (580, 704)], [(542, 662), (579, 704)], [(542, 662), (580, 704)], [(542, 662), (580, 704)], [(542, 662), (580, 704)], [(542, 662), (580, 704)], [(542, 662), (580, 703)], [(542, 662), (581, 703)], [(542, 662), (581, 703)], [(542, 662), (581, 703)], [(542, 662), (582, 704)], [(542, 662), (581, 703)], [(542, 662), (581, 704)], [(542, 661), (580, 704)], [(542, 661), (580, 703)], [(542, 661), (580, 703)], [(542, 661), (579, 703)], [(543, 660), (579, 702)], [(545, 658), (582, 700)], [(552, 654), (590, 694)], [(567, 648), (609, 690)], [(586, 642), (628, 683)], [(610, 635), (651, 676)], [(632, 630), (673, 670)], [(657, 626), (698, 668)], [(682, 631), (709, 672)], [(696, 653), (717, 675)], [(717, 638), (736, 666)], [(706, 637), (736, 674)], [(703, 638), (736, 674)], [(705, 636), (737, 673)], [(705, 637), (738, 674)], [(705, 637), (738, 674)], [(708, 637), (738, 673)], [(713, 637), (738, 673)], [(718, 642), (738, 668)], [(658, 626), (690, 663)], [(639, 621), (675, 664)], [(615, 622), (656, 668)], [(599, 627), (638, 671)], [(578, 632), (620, 677)], [(569, 637), (603, 683)], [(566, 638), (599, 683)], [(567, 639), (600, 683)], [(567, 641), (601, 682)], [(567, 640), (602, 682)], [(567, 639), (600, 682)], [(567, 638), (600, 682)], [(566, 638), (600, 685)], [(568, 634), (601, 681)], [(568, 631), (603, 678)], [(567, 632), (602, 678)], [(549, 633), (594, 678)], [(518, 629), (576, 667)], [(496, 614), (546, 651)], [(471, 589), (519, 622)], [(442, 554), (490, 594)], [(421, 537), (468, 570)], [(414, 532), (458, 561)], [(413, 535), (463, 569)], [(416, 545), (463, 586)], [(420, 567), (462, 612)], [(423, 594), (461, 639)], [(420, 618), (460, 662)], [(425, 637), (456, 678)], [(426, 657), (460, 702)], [(437, 667), (468, 705)], [(440, 665), (473, 705)], [(441, 665), (474, 705)], [(441, 664), (475, 705)], [(441, 665), (474, 706)], [(440, 667), (474, 706)], [(440, 666), (474, 706)], [(441, 667), (474, 707)], [(440, 666), (476, 706)], [(441, 667), (477, 706)], [(441, 668), (481, 706)], [(444, 669), (486, 712)], [(453, 670), (493, 716)], [(453, 671), (494, 720)], [(451, 673), (493, 720)], [(448, 673), (491, 720)], [(452, 674), (490, 720)], [(451, 674), (488, 720)], [(451, 676), (487, 720)], [(450, 676), (486, 720)], [(449, 675), (484, 720)], [(447, 675), (482, 720)], [(446, 674), (481, 720)], [(445, 673), (480, 720)], [(443, 673), (478, 720)], [(442, 673), (477, 720)], [(443, 673), (476, 720)], [(443, 673), (476, 720)], [(440, 673), (475, 720)], [(438, 674), (475, 720)], [(437, 674), (475, 720)], [(435, 674), (475, 720)], [(434, 675), (476, 720)], [(434, 676), (475, 720)], [(433, 677), (475, 720)], [(432, 678), (475, 720)], [(432, 679), (475, 720)], [(431, 679), (475, 720)], [(432, 679), (475, 720)], [(432, 681), (474, 720)], [(433, 678), (474, 720)], [(433, 676), (473, 720)], [(433, 674), (470, 720)], [(429, 672), (465, 720)], [(430, 672), (462, 720)], [(601, 135), (628, 152)], [(430, 673), (463, 720)], [(431, 676), (467, 720)], [(431, 676), (466, 720)], [(432, 682), (468, 720)], [(433, 684), (466, 720)], [(432, 684), (467, 720)], [(432, 683), (468, 720)], [(432, 684), (468, 720)], [(432, 681), (468, 720)], [(431, 677), (469, 719)], [(438, 670), (477, 711)], [(447, 663), (484, 706)], [(448, 661), (487, 711)], [(450, 662), (483, 713)], [(451, 660), (486, 712)], [(452, 662), (488, 711)], [(452, 663), (492, 710)], [(453, 664), (491, 710)], [(453, 667), (490, 710)], [(453, 666), (490, 710)], [(452, 664), (490, 710)], [(452, 662), (486, 710)], [(451, 662), (487, 711)], [(451, 662), (486, 711)], [(451, 662), (486, 711)], [(451, 662), (486, 711)], [(451, 662), (487, 711)], [(452, 662), (488, 710)], [(453, 663), (489, 710)], [(453, 665), (490, 710)], [(453, 665), (489, 710)], [(452, 664), (489, 710)], [(453, 662), (489, 710)], [(453, 662), (489, 711)], [(453, 662), (490, 710)], [(454, 661), (490, 710)], [(455, 661), (491, 710)], [(455, 662), (492, 710)], [(455, 662), (492, 709)], [(455, 662), (492, 709)], [(455, 662), (492, 709)], [(455, 661), (491, 709)], [(456, 661), (492, 709)], [(459, 659), (497, 706)], [(473, 656), (510, 702)], [(489, 651), (529, 697)], [(506, 647), (549, 693)], [(529, 643), (568, 689)], [(549, 641), (586, 687)], [(569, 640), (599, 686)], [(576, 641), (608, 687)], [(577, 642), (610, 687)], [(578, 642), (612, 687)], [(578, 643), (613, 686)], [(577, 643), (613, 686)], [(578, 643), (613, 685)], [(577, 643), (613, 685)], [(578, 643), (613, 685)], [(577, 643), (613, 685)], [(578, 643), (613, 685)], [(578, 643), (613, 685)], [(578, 643), (613, 685)], [(578, 643), (614, 686)], [(578, 643), (614, 686)], [(578, 644), (614, 686)], [(579, 643), (614, 686)], [(578, 643), (614, 685)], [(579, 643), (614, 685)], [(579, 643), (614, 685)], [(579, 643), (615, 685)]]]
def draw_track(order):    
    
    
    web = cv2.VideoCapture(0)
    index = 0
    while(True):
        
        # Capture frame-by-frame
        ret, frame = web.read()

        # Our operations on the frame come here
        # 
        # Display the resulting frame
        
        if (index < len(order[0])) and order[0][index] != None:
            frame = cv2.rectangle(frame,order[0][index][0],order[0][index][1],(225,0,0),2)
        if (index < len(order[1])) and order[1][index] != None:
            frame = cv2.rectangle(frame,order[1][index][0],order[1][index][1],(0,0,255),2)
        if (index < len(order[2])) and order[2][index] != None:    
            frame = cv2.rectangle(frame,order[2][index][0],order[2][index][1],(0,255,0),2)
        if (index < len(order[3])) and order[3][index] != None:    
            frame = cv2.rectangle(frame,order[3][index][0],order[3][index][1],(104,161,166),2)
        index += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        flipped_image = cv2.flip( frame, 1 )
        cv2.imshow("Color Tracking",flipped_image)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


draw_track(order)