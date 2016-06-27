import unittest
from math import *
from task import robot

expected_values = [[0.00000,   26.00000, 1.57080,  0.00,            -0.00],
                   [0.01365,   26.99988, 1.54349,  0.0199920063936, -0.49980015984],
                   [0.06592,   27.99840, 1.49349,  0.0662557639978, -1.35651400404],
                   [0.16804,   28.99307, 1.44349,  0.11371377594,   -1.84900793853],
                   [0.31973,   29.98139, 1.39349,  0.150965199558,  -2.06842334984],
                   [0.52064,   30.96090, 1.34349,  0.177962397159,  -2.18458193562],
                   [0.77025,   31.92914, 1.29349,  0.194670934301,  -2.19733740012],
                   [1.06793,   32.88369, 1.24349,  0.201069537222,  -2.10667441603],
                   [1.41296,   33.82218, 1.19349,  0.197150066653,  -1.91270860801],
                   [1.80445,   34.74224, 1.14349,  0.182917507815,  -1.61568669556],
                   [2.24145,   35.64159, 1.09349,  0.158389976536,  -1.21598679617],
                   [2.71993,   36.51960, 1.05016,  0.123598741553,  -0.714118890791],
                   [3.22162,   37.38464, 1.04034,  0.0819185325749, -0.193982191079],
                   [3.72989,   38.24584, 1.03489,  0.0534900673802, -0.10847369588],
                   [4.25610,   39.09613, 0.99837,  0.0573263088422, -0.630806710352],
                   [4.81855,   39.92283, 0.94837,  0.0800789573513, -1.14207930115],
                   [5.42162,   40.72039, 0.89837,  0.0994363512419, -1.28472442078],
                   [6.06380,   41.48681, 0.84837,  0.108633341303,  -1.22428826394],
                   [6.74348,   42.22017, 0.79837,  0.107658108503,  -1.06195259304],
                   [7.45896,   42.91865, 0.74837,  0.0965119056912, -0.797926014729],
                   [8.19955,   43.59058, 0.72529,  0.075209059113,  -0.432547892458],
                   [8.95301,   44.24807, 0.70967,  0.057232780393,  -0.302683623129],
                   [9.72345,   44.88548, 0.67270,  0.0598086737912, -0.636725138885],
                   [10.52084,  45.48877, 0.62270,  0.0759897991992, -1.00261487311],
                   [11.34739,  46.05146, 0.57270,  0.0885590115358, -1.07412830041],
                   [12.20102,  46.57213, 0.52270,  0.0909872822336, -0.946296882803],
                   [13.07810,  47.05231, 0.47911,  0.0832714854916, -0.716977903787],
                   [13.97122,  47.50208, 0.45393,  0.0686279513107, -0.466626500394],
                   [14.87526,  47.92947, 0.42930,  0.0594834635085, -0.457667318051],
                   [15.79372,  48.32476, 0.38354,  0.0653340327104, -0.741098865133],
                   [16.73003,  48.67564, 0.33354,  0.0758860838852, -0.917141606473],
                   [17.68271,  48.97928, 0.28354,  0.0784395091069, -0.822696469394],
                   [18.64733,  49.24274, 0.24969,  0.0708688175334, -0.595127801731],
                   [19.61934,  49.47756, 0.22440,  0.0612581321519, -0.468421040796],
                   [20.59811,  49.68224, 0.18791,  0.0619725027257, -0.630440585864],
                   [21.58477,  49.84441, 0.13791,  0.0716912865403, -0.862694622622],
                   [22.57830,  49.95707, 0.08791,  0.0780497190628, -0.875873678465],
                   [23.57595,  50.02443, 0.04694,  0.0742847231351, -0.686372292436],
                   [24.57538,  50.05743, 0.01906,  0.0649194975067, -0.508716590641],
                   [25.57533,  50.06110, 6.27146,  0.0610252441975, -0.551838642337],
                   [26.57485,  50.03183, 6.23637,  0.061095707937,  -0.612014035463],
                   [27.57389,  49.98806, 6.24243,  0.0318305895701,  0.120670879803],
                   [28.57366,  49.97184, 0.00832, -0.0119426755486,  0.776025732267],
                   [29.57337,  49.99463, 0.03727, -0.0281604433323,  0.524870950079],
                   [30.57291,  50.02448, 0.02245, -0.00537140875948,-0.288121430998],
                   [31.57284,  50.02619, 6.26415,  0.024482677159,  -0.692638060368],
                   [32.57248,  49.99976, 6.24936,  0.0261876266431, -0.287450508691],
                   [33.57219,  49.97648, 6.27043, -0.000239463375792,0.398800984041],
                   [34.57214,  49.98026, 0.02033, -0.0235237803063,  0.58450255702],
                   [35.57185,  50.00413, 0.02740, -0.0197357297608,  0.140536539426],
                   [36.57169,  50.02098, 0.00631,  0.00412748549346,-0.399223083749],
                   [37.57164,  50.01482, 6.26456,  0.0209816904766, -0.462629979512],
                   [38.57144,  49.99480, 6.26176,  0.0148220461863, -0.0558257975097],
                   [39.57135,  49.98257, 6.28015, -0.00520176363523, 0.352374783676],
                   [40.57132,  49.98888, 0.01565, -0.0174304866369,  0.357735711393],
                   [41.57120,  50.00453, 0.01648, -0.0111212702526,  0.016574456761],
                   [42.57115,  50.01382, 0.00210,  0.00453293934653,-0.280142537452],
                   [43.57112,  50.00880, 6.27104,  0.0138236569379, -0.277597333248],
                   [44.57105,  49.99665, 6.27041,  0.00879806609217,-0.0125967982363],
                   [45.57102,  49.98935, 6.28136, -0.00335115900699, 0.215749966557],
                   [46.57101,  49.99301, 0.00915, -0.0106514280427,  0.216018315964],
                   [47.57097,  50.00216, 0.00990, -0.0069867400186,  0.0148970798241],
                   [48.57095,  50.00805, 0.00188,  0.00216390508083,-0.1588987273],
                   [49.57094,  50.00567, 6.27654,  0.00805329449584,-0.168873786183],
                   [50.57091,  49.99851, 6.27549,  0.00567405929998,-0.0210520650619],
                   [51.57090,  49.99389, 6.28164, -0.00149394419282, 0.12245949432],
                   [52.57090,  49.99563, 0.00502, -0.00611148168858, 0.130377879322],
                   [53.57089,  50.00064, 0.00590, -0.00437412157885, 0.0176808141426],
                   [54.57088,  50.00450, 0.00181,  0.000641263368401,-0.0816434078927],
                   [55.57088,  50.00373, 6.27984,  0.00449515758106, -0.102759989001],
                   [56.57087,  49.99973, 6.27855,  0.00372535194535, -0.0257064349178],
                   [57.57086,  49.99667, 6.28168, -0.000265326856493, 0.0625134505925],
                   [58.57086,  49.99715, 0.00247, -0.0033339376576, 0.0793685385926],
                   [59.57086,  50.00015, 0.00353, -0.00284928917591, 0.0212231645338],
                   [60.57086,  50.00252, 0.00120,  0.000154404194063, -0.0465994424903],
                   [61.57085,  50.00220, 6.28135,  0.00252292820562, -0.0607571422296],
                   [62.57085,  50.00037, 6.28048,  0.00220482471616, -0.0172766948197],
                   [63.57085,  49.99826, 6.28168,  0.000365921809191, 0.0239243255126],
                   [64.57085,  49.99798, 0.00094, -0.00173867887543, 0.0489557990235],
                   [65.57085,  49.99953, 0.00216, -0.00202018521617, 0.0244244472728],
                   [66.57085,  50.00170, 0.00123, -0.00046608605021, -0.0186506269873],
                   [67.57085,  50.00169, 6.28194,  0.00169874477855, -0.0494599102169],
                   [68.57085,  50.00045, 6.28110,  0.00169343079205, -0.0168545981229],
                   [69.57084,  49.99836, 6.28181,  0.000450610106775, 0.0141362092113],
                   [70.57084,  49.99818, 0.00100, -0.00163501910181, 0.0476346291469],
                   [71.57084,  49.99971, 0.00206, -0.00182202497018, 0.0210253377274],
                   [72.57084,  50.00126, 0.00105, -0.000291553378929, -0.0200415400795],
                   [73.57084,  50.00142, 6.28244,  0.00126352350424, -0.0359613882898],
                   [74.57084,  50.00067, 6.28162,  0.00141807300395, -0.0164989725351],
                   [75.57084,  49.99910, 6.28184,  0.000673200135921, 0.00444109166118],
                   [76.57083,  49.99448, 6.27528,  0.0056198373117, -0.130397930754],
                   [77.57018,  49.96158, 6.22528,  0.0437891300386, -1.01043069129],
                   [78.56664,  49.87878, 6.17528,  0.0935524754094, -1.68197493466],
                   [79.55772,  49.74628, 6.12528,  0.133138173426, -1.9251672045],
                   [80.54094,  49.56441, 6.07528,  0.162495508275, -2.06531510548],
                   [81.51384,  49.33363, 6.02528,  0.181586973799, -2.10224172085],
                   [82.47399,  49.05451, 5.97528,  0.190388227148, -2.03590107172],
                   [83.41898,  48.72776, 5.92528,  0.188888058822, -1.86637806333],
                   [84.34647,  48.35418, 5.87528,  0.177088378909, -1.5938885904],
                   [85.25413,  47.93471, 5.82528,  0.15500421943, -1.21877980211],
                   [86.14067,  47.47226, 5.77949,  0.122663752801, -0.741530528573],
                   [87.01382,  46.98482, 5.76855,  0.0822097701142, -0.215287960843],
                   [87.88309,  46.49047, 5.76366,  0.0532237175086, -0.0974463860013],
                   [88.74234,  45.97903, 5.72892,  0.0562253391106, -0.607277715137],
                   [89.57912,  45.43168, 5.67892,  0.0793104555002, -1.13938130085],
                   [90.38750,  44.84319, 5.62892,  0.0998873582557, -1.30752712389],
                   [91.16545,  44.21503, 5.57892,  0.110302603075, -1.25925470304],
                   [91.91104,  43.54878, 5.52892,  0.11054280735, -1.10903113763],
                   [92.62239,  42.84610, 5.47892,  0.100607662576, -0.857049454145],
                   [93.30603,  42.11631, 5.45137,  0.080509933975, -0.503633410736],
                   [93.97320,  41.37143, 5.43425,  0.0614984501119, -0.329812243173],
                   [94.62161,  40.61019, 5.40159,  0.0600481134645, -0.578726084933],
                   [95.23797,  39.82286, 5.35159,  0.0736059601889, -0.939427302755],
                   [95.81421,  39.00571, 5.30159,  0.0857087901091, -1.03863034989],
                   [96.34889,  38.16078, 5.25159,  0.0876753069464, -0.906250822022],
                   [96.84513,  37.29267, 5.21177,  0.0795029784288, -0.672444856524],
                   [97.31295,  36.40888, 5.18670,  0.0662959737314, -0.464854666854],
                   [97.75691,  35.51287, 5.15814,  0.0605355800732, -0.518949895857],
                   [98.16532,  34.60018, 5.10814,  0.0678590913781, -0.788443583356],
                   [98.52759,  33.66822, 5.05814,  0.0757931245029, -0.8769417419],
                   [98.84646,  32.72050, 5.01574,  0.0736072196222, -0.703283623013],
                   [99.13136,  31.76198, 4.98688,  0.0651060298688, -0.523542452385],
                   [99.38779,  30.79546, 4.95656,  0.0608692646873, -0.54514116915],
                   [99.60637,  29.81974, 4.90899,  0.066940633941, -0.760476878215],
                   [99.77711,  28.83453, 4.85899,  0.0739587058133, -0.844858136219],
                   [99.90263,  27.84251, 4.81751,  0.0720756502521, -0.692510669102],
                   [99.99307,  26.84664, 4.78839,  0.0643385644523, -0.527329357527],
                   [100.05319, 25.84849, 4.75670,  0.0611996640144, -0.564913133574],
                   [100.07322, 24.84879, 4.70813,  0.0675576191349, -0.770945518158],
                   [100.04396, 23.84932, 4.65813,  0.0736735740262, -0.82847506363],
                   [99.97059,  22.85208, 4.61976,  0.070385366224, -0.654530545208],
                   [99.86404,  21.85780, 4.59151,  0.0628001154397, -0.514222392632],
                   [99.72640,  20.86737, 4.55708,  0.0618056625675, -0.603139832592],
                   [99.54708,  19.88369, 4.50708,  0.0693690112361, -0.80714034239],
                   [99.31882,  18.91019, 4.45708,  0.0746018512093, -0.82451111169],
                   [99.04892,  17.94736, 4.42109,  0.0697167701724, -0.623891486171],
                   [98.74875,  16.99351, 4.39394,  0.0617246681708, -0.497365151684],
                   [98.41857,  16.04965, 4.35781,  0.062065023128, -0.625755555638],
                   [98.04808,  15.12092, 4.30781,  0.070666319643, -0.835682644155],
                   [97.63164,  14.21188, 4.25781,  0.0760880868666, -0.84220737702],
                   [97.17581,  13.32187, 4.22032,  0.0713895679525, -0.643417895814],
                   [96.69139,  12.44708, 4.19301,  0.0628297162082, -0.499899385917],
                   [96.18024,  11.58764, 4.15867,  0.0617665943213, -0.60171911491],
                   [95.63335,  10.75056, 4.10867,  0.0697820804466, -0.818053096345],
                   [95.04531,   9.94186, 4.05867,  0.0755185605425, -0.841232806863],
                   [94.42236,   9.15967, 4.02101,  0.0711356553438, -0.645612975458],
                   [93.77424,   8.39817, 3.99349,  0.0628060377533, -0.503116113675],
                   [93.10288,   7.65711, 3.95910,  0.0617827939515, -0.602479282488],
                   [92.40089,   6.94506, 3.90910,  0.0697055978264, -0.815898036387],
                   [91.66420,   6.26900, 3.85910,  0.0753215769505, -0.837455456368],
                   [90.89867,   5.62568, 3.82183,  0.0708184862586, -0.640638502207],
                   [90.11272,   5.00745, 3.79439,  0.0625633514024, -0.501806491183],
                   [89.30793,   4.41397, 3.75961,  0.0618518159789, -0.607845128437],
                   [88.47875,   3.85516, 3.70961,  0.0699304886425, -0.820484976378],
                   [87.62269,   3.33850, 3.65961,  0.0755036651492, -0.838634299093],
                   [86.74484,   2.85967, 3.62227,  0.0709574829414, -0.641382096298],
                   [85.85194,   2.40950, 3.59487,  0.0626300864084, -0.501389916089],
                   [84.94551,   1.98726, 3.56019,  0.0618307726647, -0.606318020491],
                   [84.02207,   1.60378, 3.51019,  0.0698918398115, -0.819834405317],
                   [83.08062,   1.26693, 3.46019,  0.0755040536915, -0.839223745115],
                   [82.12531,   0.97153, 3.42278,  0.07099690762, -0.642361885128],
                   [81.16090,   0.70724, 3.39535,  0.0626703176269, -0.501804326373],
                   [80.18878,   0.47300, 3.36074,  0.0618200942114, -0.605447590882],
                   [79.20767,   0.28008, 3.31074,  0.0698490039921, -0.81892368663],
                   [78.21814,   0.13645, 3.26074,  0.0754613324773, -0.838798252052],
                   [77.22324,   0.03616, 3.22337,  0.0709543689495, -0.641939236578],
                   [76.22559,  -0.03184, 3.19593,  0.062644504693, -0.501797083083],
                   [75.22632,  -0.06885, 3.16128,  0.0618277634572, -0.606026516033],
                   [74.22644,  -0.06354, 3.11128,  0.069868962555, -0.819307612017],
                   [73.22750,  -0.01824, 3.08128,  0.0635374244233, -0.540401172257],
                   [72.22863,   0.02849, 3.10840,  0.018244730271, 0.496943109574],
                   [71.22876,   0.03668, 3.15840, -0.0284875837802, 0.985860548571],
                   [70.22925,   0.00655, 3.18505, -0.0366789157182, 0.489659136251],
                   [69.22982,  -0.02673, 3.16471, -0.00655288355394, -0.386361646924],
                   [68.22992,  -0.02577, 3.11657,  0.0267254360351, -0.766429154187],
                   [67.23041,   0.00545, 3.10415,  0.0257712676876, -0.243400151664],
                   [66.23071,   0.02848, 3.13298, -0.00545489890037, 0.522941487824],
                   [65.23081,   0.01886, 3.16945, -0.0284797426994, 0.630170083978],
                   [64.23123,  -0.01010, 3.17166, -0.0188618629526, 0.0443504333259],
                   [63.23138,  -0.02534, 3.14201,  0.0100965132369, -0.535340775213],
                   [62.23149,  -0.01268, 3.11585,  0.0253394371831, -0.482038231025],
                   [61.23179,   0.01148, 3.11901,  0.0126762566337, 0.0631851419041],
                   [60.23186,   0.02114, 3.14487, -0.0114836349915, 0.477234724292],
                   [59.23195,   0.00856, 3.16347, -0.0211362067355, 0.356150643515],
                   [58.23214,  -0.01073, 3.15830, -0.00856182037331, -0.1029975917],
                   [57.23218,  -0.01696, 3.13736,  0.0107281381352, -0.396630758979],
                   [56.23225,  -0.00599, 3.12389,  0.0169643925677, -0.263187742164],
                   [55.23236,   0.00909, 3.12914,  0.0059944761888, 0.104603983795],
                   [54.23238,   0.01334, 3.14554, -0.00908641901697, 0.317077618256],
                   [53.23243,   0.00439, 3.15553, -0.0133394325756, 0.197189529136],
                   [52.23249,  -0.00728, 3.15101, -0.00439428924579, -0.0902342574893],
                   [51.23251,  -0.01037, 3.13835,  0.0072833796057, -0.247998828829],
                   [50.23253,  -0.00335, 3.13079,  0.0103690153199, -0.149974688913],
                   [49.23257,   0.00565, 3.13439,  0.0033467337216, 0.0718668867589],
                   [48.23258,   0.00801, 3.14409, -0.00565345739415, 0.191537440678],
                   [47.23260,   0.00261, 3.14988, -0.00800612633662, 0.115351297503],
                   [46.23262,  -0.00430, 3.14714, -0.00261433358108, -0.0547335555224],
                   [45.23262,  -0.00616, 3.13975,  0.00430436988654, -0.14682425088],
                   [44.23263,  -0.00207, 3.13527,  0.00615620659715, -0.0893396166308],
                   [43.23265,   0.00324, 3.13730,  0.00207139975038, 0.0405581051979],
                   [42.23265,   0.00472, 3.14292, -0.00323833874279, 0.112029464825],
                   [41.23266,   0.00165, 3.14640, -0.00472107891341, 0.0694518916933],
                   [40.23266,  -0.00242, 3.14492, -0.00165222082347, -0.0295106631143],
                   [39.23267,  -0.00361, 3.14065,  0.00241774560743, -0.0852269525379],
                   [38.23267,  -0.00132, 3.13795,  0.00361389397082, -0.0540811651591],
                   [37.23267,   0.00180, 3.13901,  0.00132084978213, 0.021187165009],
                   [36.23267,   0.00276, 3.14225, -0.00179578232701, 0.0647073049072],
                   [35.23268,   0.00106, 3.14435, -0.00276271648232, 0.042131177153],
                   [34.23268,  -0.00171, 3.14360, -0.00105580510632, -0.0150456195769],
                   [33.23268,  -0.00225, 3.14067,  0.00170500698199, -0.0584622511446],
                   [32.23268,  -0.00057, 3.13914,  0.00225026092966, -0.0306814185115],
                   [31.23268,   0.00189, 3.14012,  0.00056501614813, 0.0196285102416],
                   [30.23269,   0.00197, 3.14291, -0.00188750337406, 0.0556628265735],
                   [29.23269,   0.00013, 3.14395, -0.00196546411848, 0.0208240523512],
                   [28.23269,  -0.00157, 3.14264, -0.000129739790282, -0.0262384670202],
                   [27.23269,  -0.00158, 3.14058,  0.0015705490332, -0.0412098226843],
                   [26.23269,  -0.00057, 3.13977,  0.00158389737652, -0.0160391989149],
                   [25.23269,   0.00125, 3.14025,  0.000566416729579, 0.00959804240832],
                   [24.23269,   0.00160, 3.14225, -0.00125309181144, 0.0398235462297],
                   [23.23272,   0.00795, 3.12823,  0.010176670085, -0.273213129297],
                   [22.23356,   0.04629, 3.07823,  0.0544582132708, -1.20880528049],
                   [21.23756,   0.13453, 3.02823,  0.106585224842, -1.84775742199],
                   [20.24722,   0.27243, 2.97823,  0.148510752479, -2.11399043935],
                   [19.26501,   0.45966, 2.92823,  0.18018118035, -2.27686822155],
                   [18.29339,   0.69574, 2.87823,  0.201556128092, -2.33618549704],
                   [17.33477,   0.98009, 2.82823,  0.212608400704, -2.29186809622],
                   [16.39157,   1.31200, 2.77823,  0.213323954952, -2.14397286324],
                   [15.46614,   1.69063, 2.72823,  0.20370188207, -1.89268772747],
                   [14.56078,   2.11503, 2.67823,  0.183754406642, -1.538331935],
                   [13.67777,   2.58416, 2.62823,  0.153506901656, -1.08135644178],
                   [12.81386,   3.08774, 2.59945,  0.112997919834, -0.522344470993],
                   [11.95891,   3.60644, 2.59306,  0.0728812479575, -0.127062401435],
                   [11.10943,   4.13405, 2.57855,  0.055029658025, -0.282522731263],
                   [10.27749,   4.68873, 2.52855,  0.0666299690776, -0.840304356566],
                   [9.47431,    5.28429, 2.47855,  0.0858577846849, -1.14699508096],
                   [8.70190,    5.91925, 2.42855,  0.0949468071368, -1.08580340815],
                   [7.96219,    6.59202, 2.37855,  0.0938853386001, -0.922931357951],
                   [7.25300,    7.29696, 2.33986,  0.0826747447657, -0.658588540142],
                   [6.56594,    8.02352, 2.31666,  0.0669828880784, -0.434451030473],
                   [5.89748,    8.76723, 2.28927,  0.0602323635014, -0.50106576636],
                   [5.25833,    9.53618, 2.23927,  0.068090106661, -0.798767214002],
                   [4.65842,   10.33611, 2.18927,  0.0771445554797, -0.907262287079],
                   [4.09760,   11.16395, 2.14318,  0.0760768029255, -0.744751740941],
                   [3.56835,   12.01237, 2.11389,  0.0668420718692, -0.529899752847],
                   [3.06312,   12.87531, 2.08706,  0.0598078407618, -0.492564941008],
                   [2.58864,   13.75549, 2.04336,  0.0646141854734, -0.718237025407],
                   [2.15592,   14.65690, 1.99336,  0.0740490844614, -0.882014329434],
                   [1.76879,   15.57882, 1.94336,  0.0765170630558, -0.802190309475],
                   [1.41990,   16.51593, 1.91104,  0.0688639753062, -0.573843436817],
                   [1.09806,   17.46270, 1.88592,  0.0599391054845, -0.46551800752],
                   [0.80649,   18.41918, 1.84745,  0.0621975613471, -0.655852451411],
                   [0.55751,   19.38759, 1.79745,  0.0725586273996, -0.881002264782],
                   [0.35725,   20.36722, 1.74745,  0.0785658596796, -0.875767080996],
                   [0.20157,   21.35496, 1.70679,  0.0744488545842, -0.682733469412],
                   [0.07972,   22.34748, 1.67912,  0.064882834359, -0.505338040211],
                   [-0.01304,  23.34313, 1.64826,  0.061049873916, -0.553004332516],
                   [-0.06571,  24.34164, 1.59874,  0.0678549982968, -0.780626848679],
                   [-0.06865,  25.34153, 1.54874,  0.0743567249518, -0.841093149344],
                   [-0.02724,  26.34061, 1.51000,  0.0709782942256, -0.659106481363],
                   [0.04757,   27.33777, 1.48182,  0.063119460403, -0.513312096691],
                   [0.15330,   28.33212, 1.44793,  0.0616984523553, -0.595669402838],
                   [0.30061,   29.32110, 1.39793,  0.0691393621112, -0.80300726745],
                   [0.49717,   30.30149, 1.34793,  0.0745240211471, -0.82601009701],
                   [0.73581,   31.27254, 1.31171,  0.0697908818285, -0.626911728507],
                   [1.00515,   32.23555, 1.28446,  0.061835776281, -0.499031179596],
                   [1.30478,   33.18955, 1.24849,  0.0620441221825, -0.623566410349],
                   [1.64511,   34.12975, 1.19849,  0.0705426713923, -0.832904952069],
                   [2.03201,   35.05176, 1.14849,  0.0759450662275, -0.840486584804],
                   [2.45881,   35.95604, 1.11115,  0.0712274025672, -0.641509070767],
                   [2.91462,   36.84608, 1.08385,  0.0627231024301, -0.499666522244],
                   [3.39770,   37.72160, 1.04934,  0.0617977174441, -0.604096399653],
                   [3.91731,   38.57588, 0.99934,  0.0698708459364, -0.819805386748],
                   [4.47896,   39.40313, 0.94934,  0.0755772432128, -0.841368391275],
                   [5.07634,   40.20501, 0.91169,  0.0711641624636, -0.645445413398],
                   [5.69954,   40.98703, 0.88419,  0.0628108807278, -0.50280958124],
                   [6.34663,   41.74939, 0.84981,  0.061780505889, -0.60234943631],
                   [7.02525,   42.48373, 0.79981,  0.0697109430389, -0.816065987638],
                   [7.73973,   43.18325, 0.74981,  0.0753393241485, -0.837818958128],
                   [8.48409,   43.85094, 0.71250,  0.0708486070103, -0.641125313031],
                   [9.24969,   44.49420, 0.68506,  0.0625868605359, -0.501942408244],
                   [10.03491,  45.11334, 0.65031,  0.0618453130503, -0.607329918217],
                   [10.84561,  45.69863, 0.60031,  0.0699086727467, -0.820037122913],
                   [11.68454,  46.24266, 0.55031,  0.0754856765425, -0.838511822363],
                   [12.54647,  46.74959, 0.51298,  0.0709433501728, -0.641298606182],
                   [13.42437,  47.22836, 0.48557,  0.0626230836657, -0.50142683905],
                   [14.31669,  47.67965, 0.45089,  0.0618329632451, -0.606477826142],
                   [15.22727,  48.09274, 0.40089,  0.0698961031285, -0.819908129536],
                   [16.15735,  48.45980, 0.35089,  0.0755044674977, -0.839170140515],
                   [17.10263,  48.78589, 0.31349,  0.0709934713204, -0.642269770544],
                   [18.05800,  49.08119, 0.28606,  0.0626666272713, -0.501763611977],
                   [19.02206,  49.34670, 0.25144,  0.0618210713724, -0.605527375241],
                   [19.99643,  49.57119, 0.20144,  0.0698530204273, -0.819009440096],
                   [20.98080,  49.74670, 0.15144,  0.0754654315531, -0.83884048242],
                   [21.97194,  49.87905, 0.11406,  0.0709585441457, -0.641982130346],
                   [22.96688,  49.97922, 0.08663,  0.0626470778005, -0.501798782828],
                   [23.96443,  50.04847, 0.05198,  0.0618270031005, -0.605968910504],
                   [24.96396,  50.07545, 0.00198,  0.0698669464503, -0.819268614751],
                   [25.96359,  50.05243, 6.23517,  0.0754709995844, -0.838770792854],
                   [26.96221,  49.99992, 6.22613,  0.0524312264672, -0.178715667915],
                   [27.96159,  49.96788, 6.27613, -7.88150333264e-05, 0.788438772841],
                   [28.96133,  49.98583, 0.04295, -0.0321204459081, 0.801828922202],
                   [29.96054,  50.02556, 0.03654, -0.0141737350406, -0.127463312606],
                   [30.96036,  50.03710, 6.26973,  0.0255613245898, -0.851639140353],
                   [31.95992,  50.00852, 6.23947,  0.0371015043079, -0.54411773885],
                   [32.95930,  49.97376, 6.25736,  0.00852210437821, 0.343469955163],
                   [33.95920,  49.97285, 0.02401, -0.0262396838876, 0.783823662862],
                   [34.95870,  50.00419, 0.03867, -0.027146301648, 0.285062282885],
                   [35.95836,  50.02881, 0.01057,  0.0041890553431, -0.511920908297],
                   [36.95826,  50.02008, 6.25517,  0.0288055233431, -0.657302253432],
                   [37.95782,  49.99032, 6.25166,  0.0200840750532, -0.0700190261819],
                   [38.95764,  49.97389, 6.28186, -0.00968173524194, 0.543304506846],
                   [39.95753,  49.98647, 0.02647, -0.0261056767725, 0.507415890685],
                   [40.95722,  50.01160, 0.02381, -0.0135341819208, -0.0532306035686],
                   [41.95713,  50.02198, 6.28013,  0.0116026444912, -0.493078841091],
                   [42.95703,  50.00907, 6.26042,  0.0219758686422, -0.375357048688],
                   [43.95683,  49.98889, 6.26559,  0.00906544713366, 0.103001851292],
                   [44.95679,  49.98227, 0.00436, -0.0111109337112, 0.413755049785],
                   [45.95671,  49.99373, 0.01855, -0.0177267604396, 0.276505005322],
                   [46.95659,  50.00954, 0.01307, -0.00627118895443, -0.109121682734],
                   [47.95656,  50.01398, 6.27899,  0.00953948171244, -0.332554877127],
                   [48.95652,  50.00455, 6.26852,  0.0139772893026, -0.20634000688],
                   [49.95644,  49.99229, 6.27334,  0.0045478208322, 0.0959638187346],
                   [50.95643,  49.98912, 0.00350, -0.00770800319705, 0.260917392409],
                   [51.95640,  49.99656, 0.01139, -0.0108825274272, 0.156443137725],
                   [52.95635,  50.00601, 0.00752, -0.00343876510277, -0.0772687838393],
                   [53.95634,  50.00841, 6.28047,  0.00601266651859, -0.201898139506],
                   [54.95633,  50.00268, 6.27443,  0.0084114853929, -0.120097137044],
                   [55.95630,  49.99541, 6.27740,  0.00267623660709, 0.0592663657163],
                   [56.95629,  49.99353, 0.00203, -0.00459253647864, 0.154956961072],
                   [57.95628,  49.99788, 0.00668, -0.00647274278703, 0.092930522496],
                   [58.95627,  50.00346, 0.00448, -0.00211776727409, -0.0441469599532],
                   [59.95627,  50.00497, 6.28172,  0.0034627784936, -0.118335971451],
                   [60.95626,  50.00169, 6.27810,  0.00496667372275, -0.0722251656647],
                   [61.95625,  49.99741, 6.27971,  0.00168951771067, 0.0322621630744],
                   [62.95625,  49.99620, 0.00104, -0.00258957378412, 0.0900821102631],
                   [63.95625,  49.99865, 0.00386, -0.00380367920818, 0.0562483734426],
                   [64.95624,  50.00193, 0.00270, -0.00135193075016, -0.0232569193686],
                   [65.95624,  50.00291, 6.28245,  0.0019259813256, -0.0684284943924],
                   [66.95624,  50.00108, 6.28026,  0.00290898349863, -0.0438348675817],
                   [67.95623,  49.99816, 6.28109,  0.00108202607595, 0.0165841005807],
                   [68.95623,  49.99762, 0.00102, -0.00184150269827, 0.062267958596],
                   [69.95623,  49.99944, 0.00261, -0.00237704031872, 0.031803467494],
                   [70.95623,  50.00151, 0.00153, -0.000558510494557, -0.0216928424169],
                   [71.95623,  50.00189, 6.28240,  0.00151296765796, -0.0462018488673],
                   [72.95623,  50.00049, 6.28118,  0.0018861723749, -0.024459794503],
                   [73.95623,  49.99849, 6.28198,  0.000491892099603, 0.0159952831333],
                   [74.95623,  49.99841, 0.00106, -0.00151400420956, 0.0452284867331],
                   [75.95622,  49.99947, 0.00191, -0.00158858567727, 0.0170045787883],
                   [76.95614,  49.98875, 6.25985,  0.0177493318554, -0.467562081545],
                   [77.95487,  49.94044, 6.20985,  0.0652006841674, -1.36377712635],
                   [78.94993,  49.84227, 6.15985,  0.114871389698, -1.89377447994],
                   [79.93885,  49.69449, 6.10985,  0.154330833199, -2.1351999845],
                   [80.91914,  49.49747, 6.05985,  0.183528577596, -2.27325194192],
                   [81.88836,  49.25170, 6.00985,  0.202427406192, -2.30775649085],
                   [82.84409,  48.95780, 5.95985,  0.211003276553, -2.23867082094],
                   [83.78393,  48.61650, 5.90985,  0.209245290847, -2.06608312289],
                   [84.70554,  48.22866, 5.85985,  0.197155682431, -1.79021269806],
                   [85.60662,  47.79523, 5.80985,  0.174749818594, -1.41141022838],
                   [86.48491,  47.31732, 5.75985,  0.142056219486, -0.930158208258],
                   [87.34650,  46.80974, 5.74176,  0.0991165933539, -0.347071541551],
                   [88.20268,  46.29306, 5.73868,  0.0619345735952, -0.061615439572],
                   [89.05217,  45.76550, 5.71623,  0.0540416639161, -0.422022993975],
                   [89.88193,  45.20757, 5.66623,  0.0732859304075, -1.02152330145],
                   [90.68278,  44.60887, 5.61623,  0.0961759668563, -1.3051102153],
                   [91.45269,  43.97089, 5.56623,  0.108909091119, -1.28008777513],
                   [92.18976,  43.29523, 5.51623,  0.111468938951, -1.15308710698],
                   [92.89214,  42.58357, 5.46623,  0.103852222567, -0.924271479924],
                   [93.56415,  41.84309, 5.43246,  0.0860687266534, -0.593934827824],
                   [94.21636,  41.08507, 5.41333,  0.0662586576726, -0.365435542015],
                   [94.85070,  40.31206, 5.38580,  0.0598878893147, -0.503317367779],
                   [95.45455,  39.51510, 5.33580,  0.0700868865737, -0.853853824622],
                   [96.01783,  38.68895, 5.28580,  0.0814050927512, -0.983824020175],
                   [96.53911,  37.83569, 5.23580,  0.082593979722, -0.843773101782],
                   [97.02396,  36.96115, 5.20142,  0.0736520157675, -0.602390698357],
                   [97.48288,  36.07270, 5.17695,  0.0623989742911, -0.455194120765],
                   [97.91538,  35.17112, 5.14241,  0.0616151448255, -0.604394006271],
                   [98.30938,  34.25213, 5.09241,  0.0712283823848, -0.856482387238],
                   [98.65696,  33.31459, 5.04241,  0.0784612214397, -0.893104800221],
                   [98.96051,  32.36185, 4.99924,  0.0755699326907, -0.712329995672],
                   [99.22981,  31.39883, 4.97089,  0.0659683285949, -0.515659224511],
                   [99.47148,  30.42851, 4.94207,  0.060499146932, -0.522953744377],
                   [99.67633,  29.44981, 4.89538,  0.0663487794693, -0.751232282754],
                   [99.83364,  28.46236, 4.84538,  0.0743309177548, -0.863041251831],
                   [99.94397,  27.46855, 4.80052,  0.0738476180698, -0.731226685423],
                   [100.01712, 26.47127, 4.77070,  0.06581874208, -0.537754280953],
                   [100.06106, 25.47227, 4.74198,  0.0603453339137, -0.521352216643],
                   [100.06816, 24.47238, 4.69701,  0.0655052215747, -0.732450530661],
                   [100.02781, 23.47330, 4.64701,  0.0737162488022, -0.860327896434],
                   [99.93915,  22.47733, 4.60021,  0.0743266100954, -0.752421520353],
                   [99.81215,  21.48546, 4.56986,  0.0664158372503, -0.545496779826],
                   [99.65662,  20.49766, 4.54259,  0.0598209154029, -0.499285326319],
                   [99.46649,  19.51598, 4.49955,  0.0643209437393, -0.710709862439],
                   [99.23092,  18.54423, 4.44955,  0.0735626584842, -0.874252306016],
                   [98.94707,  17.58547, 4.39955,  0.0761679232528, -0.800758204058],
                   [98.62399,  16.63914, 4.36724,  0.0686526872129, -0.57379833153],
                   [98.27383,  15.70248, 4.34203,  0.0598676561009, -0.466901094329],
                   [97.89398,  14.77750, 4.30342,  0.0622243638759, -0.657594255385],
                   [97.47355,  13.87029, 4.25342,  0.0725708939324, -0.88090689017],
                   [97.00830,  12.98523, 4.20342,  0.0784941805008, -0.873791103535],
                   [96.50351,  12.12207, 4.16299,  0.0742933459133, -0.679920940321]]
                   

class MotionTest(unittest.TestCase):
    
    def test_racetrack(self):
        radius = 25.0
        params = [10.0, 15.0, 0.0]

        myrobot = robot()
        myrobot.set(0.0, radius, pi / 2.0)
        speed = 1.0 # motion distance is equal to speed (we assume time = 1)
        err = 0.0
        int_crosstrack_error = 0.0
        N = 200
    
        crosstrack_error = myrobot.cte(radius)
    
        for i in range(N*2):
            diff_crosstrack_error = - crosstrack_error
            crosstrack_error = myrobot.cte(radius)
            diff_crosstrack_error += crosstrack_error
            int_crosstrack_error += crosstrack_error
            steer = - params[0] * crosstrack_error \
                    - params[1] * diff_crosstrack_error \
                    - params[2] * int_crosstrack_error
            myrobot = myrobot.move(steer, speed)
            if i >= N:
                err += crosstrack_error ** 2

            self.assertAlmostEqual(expected_values[i][0], myrobot.x, 3,
                                   "Robot X coordinate differs at point %d: "
                                   "expected %.3f, got %.3f" % (i, expected_values[i][0], myrobot.x))
            self.assertAlmostEqual(expected_values[i][1], myrobot.y, 3,
                                   "Robot Y coordinate differs at point %d: "
                                   "expected %.3f, got %.3f" % (i, expected_values[i][1], myrobot.x))
            self.assertAlmostEqual(expected_values[i][2], myrobot.orientation, 3,
                                   "Robot orientation coordinate differs at point %d: "
                                   "expected %.3f, got %.3f" % (i, expected_values[i][2], myrobot.x))
            self.assertAlmostEqual(expected_values[i][3], crosstrack_error, 3,
                                   "Crosstrack error differs at point %d: "
                                   "expected %.3f, got %.3f" % (i, expected_values[i][3], myrobot.x))
            self.assertAlmostEqual(expected_values[i][4], steer, 3,
                                   "Steering angle differs at point %d: "
                                   "expected %.3f, got %.3f" % (i, expected_values[i][4], myrobot.x))
        result = err / float(N)

        expected_result = 0.00586850481282
        if result < expected_result:
            print "INFO: your result %.14f is less than expected %.14f " % (result, expected_result), \
                  "therefore it might be accepted"
        self.assertAlmostEqual(result, expected_result, 5,
                               "Your average CTE differs from the expected one. "
                               "Expected %.5f, got %.5f" % (expected_result, result))

if __name__ == "__main__":
    unittest.main()