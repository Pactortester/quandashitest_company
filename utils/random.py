import random

from idna import unichr

chinses=[0x4e00,0x4e01,0x4e03,0x4e07,0x4e08,0x4e09,0x4e09,0x4e0a,
0x4e0b,0x4e0d,0x4e0e,0x4e10,0x4e11,0x4e13,0x4e14,0x4e16,
0x4e18,0x4e19,0x4e1a,0x4e1b,0x4e1c,0x4e1d,0x4e22,0x4e24,
0x4e25,0x4e27,0x4e2a,0x4e2d,0x4e30,0x4e32,0x4e34,0x4e38,
0x4e39,0x4e3a,0x4e3b,0x4e3d,0x4e3e,0x4e43,0x4e45,0x4e48,
0x4e49,0x4e4b,0x4e4c,0x4e4d,0x4e4e,0x4e4f,0x4e50,0x4e52,
0x4e53,0x4e54,0x4e56,0x4e58,0x4e59,0x4e5d,0x4e5e,0x4e5f,
0x4e60,0x4e61,0x4e66,0x4e70,0x4e71,0x4e73,0x4e86,0x4e88,
0x4e89,0x4e8b,0x4e8c,0x4e8e,0x4e8f,0x4e91,0x4e92,0x4e94,
0x4e95,0x4e9a,0x4e9b,0x4ea1,0x4ea4,0x4ea5,0x4ea6,0x4ea7,
0x4ea9,0x4eab,0x4eac,0x4ead,0x4eae,0x4eb2,0x4eba,0x4ebf,
0x4ec0,0x4ec1,0x4ec5,0x4ec6,0x4ec7,0x4eca,0x4ecb,0x4ecd,
0x4ece,0x4ed1,0x4ed3,0x4ed4,0x4ed6,0x4ed7,0x4ed8,0x4ed9,
0x4ee3,0x4ee4,0x4ee5,0x4eea,0x4eec,0x4ef0,0x4ef2,0x4ef6,
0x4ef7,0x4efb,0x4efd,0x4eff,0x4f01,0x4f0a,0x4f0d,0x4f0f,
0x4f10,0x4f11,0x4f17,0x4f18,0x4f19,0x4f1a,0x4f1e,0x4f1f,
0x4f20,0x4f24,0x4f26,0x4f2a,0x4f2f,0x4f30,0x4f34,0x4f36,
0x4f38,0x4f3a,0x4f3c,0x4f43,0x4f46,0x4f4d,0x4f4e,0x4f4f,
0x4f51,0x4f53,0x4f55,0x4f59,0x4f5b,0x4f5c,0x4f60,0x4f63,
0x4f69,0x4f73,0x4f7f,0x4f84,0x4f88,0x4f8b,0x4f8d,0x4f9b,
0x4f9d,0x4fa0,0x4fa3,0x4fa5,0x4fa6,0x4fa7,0x4fa8,0x4fae,
0x4faf,0x4fb5,0x4fbf,0x4fc3,0x4fc4,0x4fca,0x4fcf,0x4fd0,
0x4fd7,0x4fd8,0x4fdd,0x4fe1,0x4fe9,0x4fed,0x4fee,0x4fef,
0x4ff1,0x4ffa,0x500d,0x5012,0x5014,0x5018,0x5019,0x501a,
0x501f,0x5021,0x5026,0x503a,0x503c,0x503e,0x5047,0x504e,
0x504f,0x505a,0x505c,0x5065,0x5076,0x5077,0x507f,0x5080,
0x5085,0x508d,0x50a8,0x50ac,0x50b2,0x50bb,0x50cf,0x50da,
0x50e7,0x50f5,0x50fb,0x5112,0x5121,0x513f,0x5141,0x5143,
0x5144,0x5145,0x5146,0x5148,0x5149,0x514b,0x514d,0x5151,
0x5154,0x515a,0x515c,0x5162,0x5165,0x5168,0x516b,0x516c,
0x516d,0x5170,0x5171,0x5173,0x5174,0x5175,0x5176,0x5177,
0x5178,0x517b,0x517c,0x517d,0x5180,0x5185,0x5188,0x518c,
0x518d,0x5192,0x5195,0x5197,0x5199,0x519b,0x519c,0x51a0,
0x51a4,0x51ac,0x51af,0x51b0,0x51b2,0x51b3,0x51b5,0x51b6,
0x51b7,0x51bb,0x51c0,0x51c4,0x51c6,0x51c9,0x51cc,0x51cf,
0x51d1,0x51db,0x51dd,0x51e0,0x51e1,0x51e4,0x51eb,0x51ed,
0x51ef,0x51f0,0x51f3,0x51f6,0x51f8,0x51f9,0x51fa,0x51fb,
0x51fd,0x51ff,0x5200,0x5201,0x5203,0x5206,0x5207,0x520a,
0x5211,0x5212,0x5217,0x5218,0x5219,0x521a,0x521b,0x521d,
0x5220,0x5224,0x5228,0x5229,0x522b,0x522e,0x5230,0x5236,
0x5237,0x5238,0x5239,0x523a,0x523b,0x523d,0x5242,0x5243,
0x524a,0x524d,0x5251,0x5254,0x5256,0x5265,0x5267,0x5269,
0x526a,0x526f,0x5272,0x527f,0x5288,0x529b,0x529d,0x529e,
0x529f,0x52a0,0x52a1,0x52a3,0x52a8,0x52a9,0x52aa,0x52ab,
0x52b1,0x52b2,0x52b3,0x52bf,0x52c3,0x52c7,0x52c9,0x52cb,
0x52d2,0x52d8,0x52df,0x52e4,0x52fa,0x52fe,0x52ff,0x5300,
0x5305,0x5306,0x5308,0x5315,0x5316,0x5317,0x5319,0x5320,
0x5323,0x532a,0x5339,0x533a,0x533b,0x533e,0x533f,0x5341,
0x5343,0x5347,0x5348,0x534a,0x534e,0x534f,0x5351,0x5352,
0x5353,0x5355,0x5356,0x5357,0x535a,0x535c,0x5360,0x5361,
0x5362,0x5364,0x5366,0x5367,0x536b,0x5370,0x5371,0x5373,
0x5374,0x5375,0x5377,0x5378,0x537f,0x5382,0x5385,0x5386,
0x5389,0x538b,0x538c,0x5395,0x5398,0x539a,0x539f,0x53a2,
0x53a6,0x53a8,0x53bb,0x53bf,0x53c2,0x53c8,0x53c9,0x53ca,
0x53cb,0x53cc,0x53cd,0x53d1,0x53d4,0x53d6,0x53d7,0x53d8,
0x53d9,0x53db,0x53e0,0x53e3,0x53e4,0x53e5,0x53e6,0x53e8,
0x53ea,0x53eb,0x53ec,0x53ed,0x53ee,0x53ef,0x53f0,0x53f2,
0x53f3,0x53f6,0x53f7,0x53f8,0x53f9,0x53fc,0x53fd,0x5401,
0x5403,0x5404,0x5406,0x5408,0x5409,0x540a,0x540c,0x540d,
0x540e,0x540f,0x5410,0x5411,0x5413,0x5415,0x5417,0x541b,
0x541d,0x541e,0x541f,0x5420,0x5426,0x5427,0x5428,0x5429,
0x542b,0x542c,0x542d,0x542e,0x542f,0x5431,0x5434,0x5435,
0x5438,0x5439,0x543b,0x543c,0x5440,0x5446,0x5448,0x544a,
0x5450,0x5455,0x5458,0x545b,0x545c,0x5462,0x5468,0x5473,
0x5475,0x547b,0x547c,0x547d,0x5486,0x548c,0x548f,0x5490,
0x5492,0x5495,0x5496,0x5499,0x54a7,0x54a8,0x54aa,0x54ac,
0x54b1,0x54b3,0x54b8,0x54bd,0x54c0,0x54c1,0x54c4,0x54c6,
0x54c8,0x54cd,0x54ce,0x54d1,0x54d7,0x54df,0x54e5,0x54e8,
0x54e9,0x54ea,0x54ed,0x54ee,0x54f2,0x54fa,0x54fc,0x5501,
0x5506,0x5507,0x5509,0x5510,0x5520,0x5524,0x5527,0x552c,
0x552e,0x552f,0x5531,0x553e,0x5543,0x5544,0x5546,0x554a,
0x5561,0x5564,0x5565,0x5566,0x5570,0x5578,0x557c,0x5582,
0x5584,0x5587,0x5589,0x558a,0x5598,0x559c,0x559d,0x55a7,
0x55b3,0x55b7,0x55bb,0x55c5,0x55d3,0x55dc,0x55e1,0x55e4,
0x55e6,0x55fd,0x5600,0x5601,0x5609,0x5631,0x5632,0x5634,
0x5636,0x5639,0x563f,0x5668,0x5669,0x566a,0x568e,0x56a3,
0x56b7,0x56bc,0x56ca,0x56da,0x56db,0x56de,0x56e0,0x56e2,
0x56e4,0x56ed,0x56f0,0x56f1,0x56f4,0x56fa,0x56fd,0x56fe,
0x5703,0x5706,0x5708,0x571f,0x5723,0x5728,0x5730,0x573a,
0x573e,0x5740,0x5747,0x574a,0x574e,0x574f,0x5750,0x5751,
0x5757,0x575a,0x575b,0x575d,0x575e,0x575f,0x5760,0x5761,
0x5764,0x5766,0x576a,0x576f,0x5777,0x5782,0x5783,0x5784,
0x578b,0x5792,0x579b,0x57a2,0x57a6,0x57ab,0x57ae,0x57c2,
0x57c3,0x57cb,0x57ce,0x57df,0x57e0,0x57f9,0x57fa,0x5802,
0x5806,0x5815,0x5821,0x5824,0x582a,0x5830,0x5835,0x584c,
0x5851,0x5854,0x5858,0x585e,0x586b,0x5883,0x5885,0x5893,
0x5899,0x589e,0x58a8,0x58a9,0x58c1,0x58d5,0x58e4,0x58eb,
0x58ee,0x58f0,0x58f3,0x58f6,0x58f9,0x5904,0x5907,0x590d,
0x590f,0x5915,0x5916,0x591a,0x591c,0x591f,0x5927,0x5929,
0x592a,0x592b,0x592d,0x592e,0x592f,0x5931,0x5934,0x5937,
0x5938,0x5939,0x593a,0x5944,0x5947,0x5948,0x5949,0x594b,
0x594f,0x5951,0x5954,0x5955,0x5956,0x5957,0x5960,0x5962,
0x5965,0x5973,0x5974,0x5976,0x5978,0x5979,0x597d,0x5982,
0x5984,0x5986,0x5987,0x5988,0x5992,0x5993,0x5996,0x5999,
0x59a5,0x59a8,0x59b9,0x59bb,0x59c6,0x59ca,0x59cb,0x59d0,
0x59d1,0x59d3,0x59d4,0x59da,0x59dc,0x59e5,0x59e8,0x59fb,
0x59ff,0x5a01,0x5a03,0x5a04,0x5a07,0x5a18,0x5a1c,0x5a29,
0x5a31,0x5a36,0x5a46,0x5a49,0x5a5a,0x5a74,0x5a76,0x5a7f,
0x5a92,0x5a9a,0x5ab3,0x5ac1,0x5ac2,0x5ac9,0x5acc,0x5ae1,
0x5ae9,0x5b09,0x5b50,0x5b54,0x5b55,0x5b57,0x5b58,0x5b59,
0x5b5d,0x5b5f,0x5b63,0x5b64,0x5b66,0x5b69,0x5b75,0x5b7d,
0x5b81,0x5b83,0x5b85,0x5b87,0x5b88,0x5b89,0x5b8b,0x5b8c,
0x5b8f,0x5b97,0x5b98,0x5b99,0x5b9a,0x5b9b,0x5b9c,0x5b9d,
0x5b9e,0x5ba0,0x5ba1,0x5ba2,0x5ba3,0x5ba4,0x5ba6,0x5baa,
0x5bab,0x5bb0,0x5bb3,0x5bb4,0x5bb5,0x5bb6,0x5bb9,0x5bbd,
0x5bbe,0x5bbf,0x5bc2,0x5bc4,0x5bc6,0x5bc7,0x5bcc,0x5bd2,
0x5bd3,0x5bdd,0x5bde,0x5bdf,0x5be1,0x5be5,0x5be8,0x5bf8,
0x5bf9,0x5bfa,0x5bfb,0x5bfc,0x5bff,0x5c01,0x5c04,0x5c06,
0x5c09,0x5c0a,0x5c0f,0x5c11,0x5c14,0x5c16,0x5c18,0x5c1a,
0x5c1d,0x5c24,0x5c31,0x5c38,0x5c3a,0x5c3c,0x5c3d,0x5c3e,
0x5c3f,0x5c40,0x5c41,0x5c42,0x5c45,0x5c48,0x5c49,0x5c4a,
0x5c4b,0x5c4e,0x5c4f,0x5c51,0x5c55,0x5c5e,0x5c60,0x5c61,
0x5c65,0x5c6f,0x5c71,0x5c79,0x5c7f,0x5c81,0x5c82,0x5c94,
0x5c96,0x5c97,0x5c9b,0x5ca9,0x5cad,0x5cb3,0x5cb8,0x5ce1,
0x5ce6,0x5ced,0x5cf0,0x5cfb,0x5d07,0x5d0e,0x5d14,0x5d16,
0x5d29,0x5d2d,0x5d4c,0x5dcd,0x5ddd,0x5dde,0x5de1,0x5de2,
0x5de5,0x5de6,0x5de7,0x5de8,0x5de9,0x5deb,0x5dee,0x5df1,
0x5df2,0x5df4,0x5df7,0x5dfe,0x5e01,0x5e02,0x5e03,0x5e05,
0x5e06,0x5e08,0x5e0c,0x5e10,0x5e15,0x5e16,0x5e18,0x5e1a,
0x5e1c,0x5e1d,0x5e26,0x5e2d,0x5e2e,0x5e38,0x5e3d,0x5e45,
0x5e4c,0x5e54,0x5e55,0x5e62,0x5e72,0x5e72,0x5e73,0x5e74,
0x5e76,0x5e78,0x5e7b,0x5e7c,0x5e7d,0x5e7f,0x5e84,0x5e86,
0x5e87,0x5e8a,0x5e8f,0x5e90,0x5e93,0x5e94,0x5e95,0x5e97,
0x5e99,0x5e9c,0x5e9e,0x5e9f,0x5ea6,0x5ea7,0x5ead,0x5eb5,
0x5eb6,0x5eb7,0x5eb8,0x5ec9,0x5eca,0x5ed3,0x5ef6,0x5ef7,
0x5efa,0x5f00,0x5f02,0x5f03,0x5f04,0x5f0a,0x5f0f,0x5f13,
0x5f15,0x5f1b,0x5f1f,0x5f20,0x5f25,0x5f26,0x5f27,0x5f2f,
0x5f31,0x5f39,0x5f3a,0x5f52,0x5f53,0x5f55,0x5f62,0x5f64,
0x5f69,0x5f6a,0x5f6c,0x5f6d,0x5f70,0x5f71,0x5f79,0x5f7b,
0x5f7c,0x5f80,0x5f81,0x5f84,0x5f85,0x5f88,0x5f8a,0x5f8b,
0x5f90,0x5f92,0x5f92,0x5f97,0x5f98,0x5fa1,0x5faa,0x5fae,
0x5fb7,0x5fbd,0x5fc3,0x5fc5,0x5fc6,0x5fcc,0x5fcd,0x5fd7,
0x5fd8,0x5fd9,0x5fe0,0x5fe7,0x5feb,0x5ff1,0x5ff5,0x5ffd,
0x5fff,0x6000,0x6001,0x600e,0x6012,0x6014,0x6015,0x6016,
0x601c,0x601d,0x6020,0x6025,0x6027,0x6028,0x602a,0x602f,
0x603b,0x6043,0x604b,0x604d,0x6050,0x6052,0x6055,0x6062,
0x6064,0x6068,0x6069,0x606c,0x606d,0x606f,0x6070,0x6073,
0x6076,0x607c,0x6084,0x6089,0x608d,0x6094,0x609f,0x60a0,
0x60a3,0x60a6,0x60a8,0x60ac,0x60af,0x60b2,0x60b4,0x60bc,
0x60c5,0x60ca,0x60cb,0x60d1,0x60d5,0x60dc,0x60e0,0x60e6,
0x60e7,0x60e8,0x60e9,0x60eb,0x60ed,0x60ef,0x60f0,0x60f3,
0x60f6,0x60f9,0x6101,0x6108,0x6109,0x610f,0x6115,0x611a,
0x611f,0x6124,0x6127,0x613f,0x6148,0x614c,0x614e,0x6155,
0x6162,0x6167,0x6168,0x6170,0x6177,0x618b,0x618e,0x6194,
0x61a8,0x61be,0x61c2,0x61c8,0x61ca,0x61d2,0x61e6,0x6208,
0x620f,0x6210,0x6211,0x6212,0x6216,0x6218,0x621a,0x622a,
0x6233,0x6234,0x6237,0x623f,0x6240,0x6241,0x6247,0x624b,
0x624d,0x624e,0x6251,0x6252,0x6253,0x6254,0x6258,0x625b,
0x6263,0x6267,0x6269,0x626b,0x626c,0x626d,0x626e,0x626f,
0x6270,0x6273,0x6276,0x6279,0x627c,0x627e,0x627f,0x6280,
0x6284,0x628a,0x6291,0x6292,0x6293,0x6295,0x6296,0x6297,
0x6298,0x629a,0x629b,0x62a0,0x62a1,0x62a2,0x62a4,0x62a5,
0x62ab,0x62ac,0x62b1,0x62b5,0x62b9,0x62bc,0x62bd,0x62c2,
0x62c4,0x62c5,0x62c6,0x62c7,0x62c9,0x62cc,0x62cd,0x62d0,
0x62d2,0x62d3,0x62d4,0x62d6,0x62d7,0x62d8,0x62d9,0x62db,
0x62dc,0x62df,0x62e2,0x62e3,0x62e5,0x62e6,0x62e7,0x62e8,
0x62e9,0x62ec,0x62ed,0x62ef,0x62f1,0x62f3,0x62f4,0x62f7,
0x62fc,0x62fe,0x62ff,0x6301,0x6302,0x6307,0x6309,0x630e,
0x6311,0x6316,0x631a,0x631f,0x6320,0x6321,0x6323,0x6324,
0x6325,0x6328,0x632a,0x632b,0x632f,0x633a,0x633d,0x6342,
0x6345,0x6346,0x6349,0x634c,0x634d,0x634e,0x634f,0x6350,
0x6355,0x635e,0x635f,0x6361,0x6362,0x6363,0x6367,0x636e,
0x6376,0x6377,0x637a,0x637b,0x6380,0x6382,0x6388,0x6389,
0x638c,0x638f,0x6390,0x6392,0x6396,0x6398,0x63a0,0x63a2,
0x63a5,0x63a7,0x63a8,0x63a9,0x63aa,0x63b0,0x63b7,0x63b8,
0x63ba,0x63c9,0x63cd,0x63cf,0x63d0,0x63d2,0x63d6,0x63e1,
0x63e3,0x63e9,0x63ea,0x63ed,0x63f4,0x63fd,0x6400,0x6401,
0x6402,0x6405,0x640f,0x6413,0x6414,0x641c,0x641e,0x642a,
0x642c,0x642d,0x643a,0x6444,0x6446,0x6447,0x644a,0x6454,
0x6458,0x6467,0x6469,0x6478,0x6479,0x6487,0x6491,0x6492,
0x6495,0x649e,0x64a4,0x64a9,0x64ac,0x64ad,0x64ae,0x64b0,
0x64b5,0x64bc,0x64c2,0x64c5,0x64cd,0x64ce,0x64d2,0x64e6,
0x6500,0x6512,0x6518,0x652f,0x6536,0x6539,0x653b,0x653e,
0x653f,0x6545,0x6548,0x654c,0x654f,0x6551,0x6559,0x655b,
0x655e,0x6562,0x6563,0x6566,0x656c,0x6570,0x6572,0x6574,
0x6577,0x6587,0x658b,0x6591,0x6597,0x6599,0x659c,0x659f,
0x65a4,0x65a5,0x65a7,0x65a9,0x65ad,0x65af,0x65b0,0x65b9,
0x65bd,0x65c1,0x65c5,0x65cb,0x65cf,0x65d7,0x65e0,0x65e2,
0x65e5,0x65e6,0x65e7,0x65e8,0x65e9,0x65ec,0x65ed,0x65f1,
0x65f6,0x65f7,0x65fa,0x6602,0x6606,0x660c,0x660e,0x660f,
0x6613,0x6614,0x6619,0x661f,0x6620,0x6625,0x6627,0x6628,
0x662d,0x662f,0x6635,0x663c,0x663e,0x6643,0x664b,0x664c,
0x6652,0x6653,0x6655,0x665a,0x6664,0x6666,0x6668,0x666e,
0x666f,0x6670,0x6674,0x6676,0x667a,0x667e,0x6682,0x6687,
0x6691,0x6696,0x6697,0x66ae,0x66b4,0x66d9,0x66f2,0x66f4,
0x66f9,0x66fc,0x66fe,0x66ff,0x6700,0x6708,0x6709,0x670b,
0x670d,0x6717,0x671b,0x671d,0x671f,0x6726,0x6728,0x672a,
0x672b,0x672c,0x672f,0x6731,0x6734,0x6735,0x673a,0x673d,
0x6740,0x6742,0x6743,0x6746,0x6748,0x6749,0x674e,0x674f,
0x6750,0x6751,0x6756,0x675c,0x675f,0x6760,0x6761,0x6765,
0x6768,0x676d,0x676f,0x6770,0x677e,0x677f,0x6781,0x6784,
0x6789,0x6790,0x6795,0x6797,0x679a,0x679c,0x679d,0x67a2,
0x67a3,0x67aa,0x67ab,0x67af,0x67b6,0x67b7,0x67c4,0x67cf,
0x67d0,0x67d1,0x67d2,0x67d3,0x67d4,0x67dc,0x67e0,0x67e5,
0x67ec,0x67f1,0x67f3,0x67f4,0x67ff,0x6805,0x6807,0x6808,
0x680b,0x680f,0x6811,0x6813,0x6816,0x6817,0x6821,0x682a,
0x6837,0x6838,0x6839,0x683c,0x683d,0x6842,0x6843,0x6845,
0x6846,0x6848,0x684c,0x6850,0x6851,0x6863,0x6865,0x6866,
0x6868,0x6869,0x6876,0x6881,0x6885,0x6886,0x6897,0x68a2,
0x68a6,0x68a7,0x68a8,0x68ad,0x68af,0x68b0,0x68b3,0x68c0,
0x68c9,0x68cb,0x68cd,0x68d2,0x68d5,0x68d8,0x68da,0x68e0,
0x68ee,0x68f1,0x68f5,0x68fa,0x6905,0x690d,0x690e,0x6912,
0x692d,0x6930,0x693f,0x6954,0x695a,0x695e,0x6963,0x6977,
0x697c,0x6982,0x6984,0x6986,0x6994,0x6995,0x699b,0x699c,
0x69a8,0x69b4,0x69d0,0x69fd,0x6a0a,0x6a1f,0x6a21,0x6a2a,
0x6a31,0x6a44,0x6a58,0x6a59,0x6a61,0x6a71,0x6a80,0x6a90,
0x6aa9,0x6aac,0x6b20,0x6b21,0x6b22,0x6b23,0x6b27,0x6b32,
0x6b3a,0x6b3e,0x6b47,0x6b49,0x6b4c,0x6b62,0x6b63,0x6b64,
0x6b65,0x6b66,0x6b67,0x6b6a,0x6b79,0x6b7b,0x6b7c,0x6b83,
0x6b89,0x6b8a,0x6b8b,0x6b96,0x6bb4,0x6bb5,0x6bb7,0x6bbf,
0x6bc1,0x6bc5,0x6bcd,0x6bcf,0x6bd2,0x6bd4,0x6bd5,0x6bd9,
0x6bdb,0x6be1,0x6beb,0x6bef,0x6c0f,0x6c11,0x6c13,0x6c14,
0x6c1b,0x6c22,0x6c27,0x6c28,0x6c2e,0x6c2f,0x6c34,0x6c38,
0x6c41,0x6c42,0x6c47,0x6c49,0x6c57,0x6c5b,0x6c5e,0x6c5f,
0x6c60,0x6c61,0x6c64,0x6c6a,0x6c70,0x6c79,0x6c7d,0x6c83,
0x6c88,0x6c89,0x6c90,0x6c99,0x6c9b,0x6c9f,0x6ca1,0x6ca5,
0x6ca6,0x6ca7,0x6caa,0x6cab,0x6cae,0x6cb3,0x6cb8,0x6cb9,
0x6cbb,0x6cbc,0x6cbd,0x6cbe,0x6cbf,0x6cc4,0x6cc9,0x6cca,
0x6ccc,0x6cd5,0x6cdb,0x6cde,0x6ce1,0x6ce2,0x6ce3,0x6ce5,
0x6ce8,0x6cea,0x6cf0,0x6cf3,0x6cf5,0x6cfb,0x6cfc,0x6cfd,
0x6d01,0x6d0b,0x6d12,0x6d17,0x6d1b,0x6d1e,0x6d25,0x6d2a,
0x6d32,0x6d3b,0x6d3c,0x6d3d,0x6d3e,0x6d41,0x6d45,0x6d46,
0x6d47,0x6d4a,0x6d4b,0x6d4e,0x6d51,0x6d53,0x6d59,0x6d66,
0x6d69,0x6d6a,0x6d6e,0x6d74,0x6d77,0x6d78,0x6d82,0x6d88,
0x6d89,0x6d8c,0x6d8e,0x6d95,0x6d9b,0x6d9d,0x6da1,0x6da3,
0x6da4,0x6da6,0x6da7,0x6da8,0x6da9,0x6dae,0x6daf,0x6db2,
0x6db5,0x6dc0,0x6dc6,0x6dcb,0x6dcc,0x6dd1,0x6dd8,0x6de1,
0x6de4,0x6deb,0x6dee,0x6df1,0x6df3,0x6df7,0x6df9,0x6dfb,
0x6e05,0x6e0a,0x6e10,0x6e14,0x6e17,0x6e20,0x6e21,0x6e23,
0x6e24,0x6e29,0x6e2f,0x6e34,0x6e38,0x6e3a,0x6e43,0x6e56,
0x6e58,0x6e7e,0x6e7f,0x6e83,0x6e85,0x6e89,0x6e90,0x6e9c,
0x6ea2,0x6eaa,0x6eaf,0x6eb6,0x6eba,0x6ecb,0x6ed1,0x6ed3,
0x6ed4,0x6eda,0x6ede,0x6ee1,0x6ee4,0x6ee5,0x6ee8,0x6ee9,
0x6ef4,0x6f02,0x6f06,0x6f0f,0x6f13,0x6f14,0x6f20,0x6f29,
0x6f2b,0x6f31,0x6f3e,0x6f58,0x6f5c,0x6f66,0x6f6d,0x6f6e,
0x6f84,0x6f88,0x6f8e,0x6f9c,0x6fa1,0x6fb3,0x6fc0,0x6fd2,
0x7011,0x704c,0x706b,0x706d,0x706f,0x7070,0x7075,0x7076,
0x7078,0x707c,0x707e,0x707f,0x7089,0x708a,0x708e,0x7092,
0x7095,0x70ab,0x70ac,0x70ad,0x70ae,0x70b8,0x70b9,0x70bc,
0x70c1,0x70c2,0x70c8,0x70d8,0x70d9,0x70db,0x70df,0x70e4,
0x70e6,0x70e7,0x70eb,0x70ed,0x70f9,0x710a,0x7115,0x7119,
0x711a,0x7126,0x7130,0x7136,0x714c,0x714e,0x715e,0x7164,
0x7167,0x716e,0x7184,0x718a,0x718f,0x7194,0x7199,0x719f,
0x71ac,0x71c3,0x71ce,0x71d5,0x71e5,0x7206,0x722a,0x722c,
0x7231,0x7235,0x7236,0x7237,0x7238,0x7239,0x723d,0x7247,
0x7248,0x724c,0x724d,0x7259,0x725b,0x7261,0x7262,0x7267,
0x7269,0x7272,0x7275,0x7279,0x727a,0x7280,0x7281,0x72ac,
0x72af,0x72b6,0x72b9,0x72c2,0x72c8,0x72d0,0x72d7,0x72de,
0x72e0,0x72e1,0x72ec,0x72ed,0x72ee,0x72f0,0x72f1,0x72f8,
0x72fc,0x730e,0x7316,0x731b,0x731c,0x7329,0x732a,0x732b,
0x732c,0x732e,0x7334,0x733e,0x733f,0x7384,0x7387,0x7389,
0x738b,0x7396,0x739b,0x73a9,0x73ab,0x73af,0x73b0,0x73b2,
0x73b7,0x73bb,0x73ca,0x73cd,0x73e0,0x73ed,0x7403,0x7405,
0x7406,0x7409,0x7410,0x7422,0x7433,0x7434,0x743c,0x745e,
0x745f,0x7470,0x7483,0x74a7,0x74dc,0x74e2,0x74e3,0x74e4,
0x74e6,0x74ee,0x74f6,0x74f7,0x7518,0x751a,0x751c,0x751f,
0x7525,0x7528,0x7529,0x752b,0x7530,0x7531,0x7532,0x7533,
0x7535,0x7537,0x7538,0x753b,0x7545,0x754c,0x754f,0x7554,
0x7559,0x755c,0x7565,0x7566,0x756a,0x7574,0x7578,0x7586,
0x758f,0x7591,0x7597,0x7599,0x759a,0x759f,0x75a4,0x75ab,
0x75ae,0x75af,0x75b2,0x75b9,0x75bc,0x75be,0x75c5,0x75c7,
0x75ca,0x75d2,0x75d5,0x75d8,0x75db,0x75e2,0x75ea,0x75f0,
0x75f4,0x75f9,0x761f,0x7624,0x7626,0x7629,0x762a,0x762b,
0x7638,0x763e,0x764c,0x765e,0x7663,0x767b,0x767d,0x767e,
0x7682,0x7684,0x7686,0x7687,0x76ae,0x76b1,0x76bf,0x76c5,
0x76c6,0x76c8,0x76ca,0x76cf,0x76d0,0x76d1,0x76d2,0x76d4,
0x76d6,0x76d7,0x76d8,0x76db,0x76df,0x76ee,0x76ef,0x76f2,
0x76f4,0x76f8,0x76f9,0x76fc,0x76fe,0x7701,0x7709,0x770b,
0x771f,0x7720,0x7728,0x772f,0x7736,0x7737,0x773c,0x7740,
0x7741,0x775b,0x7761,0x7763,0x7766,0x776c,0x7779,0x7784,
0x778e,0x7792,0x77a7,0x77aa,0x77ac,0x77ad,0x77b3,0x77bb,
0x77d7,0x77db,0x77e2,0x77e5,0x77e9,0x77eb,0x77ed,0x77ee,
0x77f3,0x77fe,0x77ff,0x7801,0x7802,0x780c,0x780d,0x7814,
0x7816,0x781a,0x7830,0x7834,0x7838,0x783e,0x7840,0x7845,
0x7855,0x785d,0x786b,0x786c,0x786e,0x787c,0x7889,0x788c,
0x788d,0x788e,0x7891,0x7897,0x7898,0x789f,0x78a7,0x78b0,
0x78b1,0x78b3,0x78b4,0x78be,0x78c1,0x78c5,0x78d5,0x78e8,
0x78f7,0x78fa,0x7901,0x793a,0x793c,0x793e,0x7948,0x7956,
0x795d,0x795e,0x795f,0x7960,0x7965,0x7968,0x796d,0x7977,
0x7978,0x7980,0x7981,0x798f,0x79bb,0x79bd,0x79be,0x79c0,
0x79c1,0x79c3,0x79c6,0x79c9,0x79cb,0x79cd,0x79d1,0x79d2,
0x79d5,0x79d8,0x79df,0x79e4,0x79e6,0x79e7,0x79e9,0x79eb,
0x79ef,0x79f0,0x79f8,0x79fb,0x79fd,0x7a00,0x7a0b,0x7a0d,
0x7a0e,0x7a1a,0x7a20,0x7a33,0x7a3b,0x7a3c,0x7a3d,0x7a3f,
0x7a46,0x7a57,0x7a74,0x7a76,0x7a77,0x7a7a,0x7a7f,0x7a81,
0x7a83,0x7a84,0x7a8d,0x7a91,0x7a92,0x7a96,0x7a97,0x7a98,
0x7a9c,0x7a9d,0x7a9f,0x7aa5,0x7abf,0x7acb,0x7ad6,0x7ad9,
0x7ade,0x7adf,0x7ae0,0x7ae3,0x7ae5,0x7aed,0x7aef,0x7af9,
0x7aff,0x7b06,0x7b0b,0x7b11,0x7b14,0x7b19,0x7b1b,0x7b24,
0x7b26,0x7b28,0x7b2c,0x7b3c,0x7b49,0x7b4b,0x7b4f,0x7b50,
0x7b51,0x7b52,0x7b54,0x7b56,0x7b5b,0x7b5d,0x7b77,0x7b79,
0x7b7e,0x7b80,0x7b8d,0x7b95,0x7b97,0x7ba1,0x7ba9,0x7bab,
0x7bad,0x7bb1,0x7bc7,0x7bd3,0x7bd9,0x7be1,0x7bee,0x7bf1,
0x7bf7,0x7c07,0x7c38,0x7c3f,0x7c4d,0x7c73,0x7c7b,0x7c7d,
0x7c89,0x7c92,0x7c97,0x7c98,0x7c9f,0x7ca4,0x7ca5,0x7caa,
0x7cae,0x7cb1,0x7cb9,0x7cbe,0x7cca,0x7cd5,0x7cd6,0x7cd9,
0x7cdc,0x7cdf,0x7ce0,0x7cef,0x7cfb,0x7d0a,0x7d20,0x7d22,
0x7d27,0x7d2b,0x7d2f,0x7d6e,0x7e41,0x7ea0,0x7ea2,0x7ea4,
0x7ea6,0x7ea7,0x7eaa,0x7eab,0x7eac,0x7eaf,0x7eb1,0x7eb2,
0x7eb3,0x7eb5,0x7eb7,0x7eb8,0x7eb9,0x7eba,0x7ebd,0x7ebf,
0x7ec3,0x7ec4,0x7ec5,0x7ec6,0x7ec7,0x7ec8,0x7eca,0x7ecd,
0x7ece,0x7ecf,0x7ed1,0x7ed2,0x7ed3,0x7ed5,0x7ed8,0x7ed9,
0x7edc,0x7edd,0x7ede,0x7edf,0x7ee2,0x7ee3,0x7ee7,0x7ee9,
0x7eea,0x7eed,0x7ef0,0x7ef3,0x7ef4,0x7ef5,0x7ef7,0x7ef8,
0x7efc,0x7efd,0x7eff,0x7f00,0x7f05,0x7f06,0x7f0e,0x7f13,
0x7f14,0x7f15,0x7f16,0x7f18,0x7f1a,0x7f1d,0x7f20,0x7f24,
0x7f28,0x7f29,0x7f2d,0x7f30,0x7f34,0x7f38,0x7f3a,0x7f50,
0x7f51,0x7f55,0x7f57,0x7f5a,0x7f62,0x7f69,0x7f6a,0x7f6e,
0x7f72,0x7f8a,0x7f8e,0x7f94,0x7f9e,0x7fa1,0x7fa4,0x7fb9,
0x7fbd,0x7fc1,0x7fc5,0x7fce,0x7fd4,0x7fd8,0x7fe0,0x7fe9,
0x7ff0,0x7ffb,0x7ffc,0x8000,0x8001,0x8003,0x8005,0x800c,
0x800d,0x8010,0x8015,0x8015,0x8017,0x8019,0x8033,0x8038,
0x803b,0x803d,0x803f,0x8042,0x804a,0x804b,0x804c,0x8054,
0x8058,0x805a,0x806a,0x8083,0x8084,0x8086,0x8089,0x808b,
0x808c,0x8096,0x8098,0x809a,0x809b,0x809d,0x80a0,0x80a1,
0x80a2,0x80a4,0x80a5,0x80a9,0x80aa,0x80ae,0x80af,0x80b2,
0x80b4,0x80ba,0x80be,0x80bf,0x80c0,0x80c1,0x80c3,0x80c6,
0x80cc,0x80ce,0x80d6,0x80da,0x80dc,0x80de,0x80e1,0x80e7,
0x80ef,0x80f0,0x80f3,0x80f6,0x80f8,0x80fd,0x8102,0x8106,
0x8109,0x810a,0x810f,0x8110,0x8111,0x8113,0x8116,0x811a,
0x812f,0x8131,0x8138,0x813e,0x814a,0x814b,0x814c,0x8150,
0x8154,0x8155,0x8165,0x816e,0x8170,0x8179,0x817a,0x817b,
0x817e,0x817f,0x8180,0x818a,0x818f,0x8198,0x819b,0x819c,
0x819d,0x81a8,0x81b3,0x81c0,0x81c2,0x81ca,0x81e3,0x81ea,
0x81ed,0x81f3,0x81f4,0x81fc,0x8200,0x8205,0x8206,0x820c,
0x820d,0x8212,0x8214,0x821e,0x821f,0x822a,0x822c,0x8230,
0x8231,0x8235,0x8236,0x8237,0x8239,0x8247,0x8258,0x826f,
0x8270,0x8272,0x8273,0x827a,0x827e,0x8282,0x828b,0x828d,
0x8292,0x8299,0x829c,0x829d,0x82a5,0x82a6,0x82ac,0x82ad,
0x82af,0x82b1,0x82b3,0x82b9,0x82bd,0x82c7,0x82cd,0x82cf,
0x82d4,0x82d7,0x82db,0x82de,0x82df,0x82e5,0x82e6,0x82eb,
0x82f1,0x82f9,0x8301,0x8302,0x8303,0x8304,0x8305,0x8309,
0x830e,0x8327,0x832b,0x832c,0x8334,0x8335,0x8336,0x8338,
0x8346,0x8349,0x8350,0x8352,0x8354,0x835a,0x835e,0x8360,
0x8361,0x8363,0x8364,0x8367,0x836f,0x8377,0x8378,0x8389,
0x83ab,0x83b1,0x83b2,0x83b7,0x83b9,0x83ba,0x83bd,0x83c7,
0x83ca,0x83cc,0x83dc,0x83e0,0x83e9,0x83f1,0x83f2,0x8404,
0x840c,0x840d,0x840e,0x841d,0x8424,0x8425,0x8427,0x8428,
0x843d,0x8457,0x845b,0x8461,0x8463,0x846b,0x846c,0x8471,
0x8475,0x8482,0x848b,0x8499,0x849c,0x84b2,0x84b8,0x84bf,
0x84c4,0x84c9,0x84d6,0x84dd,0x84ec,0x8511,0x8513,0x8517,
0x851a,0x852b,0x852c,0x853c,0x853d,0x8549,0x854a,0x8574,
0x857e,0x8584,0x8587,0x859b,0x85aa,0x85af,0x85cf,0x85d0,
0x85d5,0x85e4,0x85fb,0x8611,0x8638,0x864e,0x864f,0x8650,
0x8651,0x865a,0x866b,0x8671,0x8679,0x867d,0x867e,0x8680,
0x8681,0x8682,0x868a,0x868c,0x8693,0x8695,0x869c,0x86a3,
0x86a4,0x86aa,0x86af,0x86c0,0x86c6,0x86c7,0x86c9,0x86cb,
0x86d4,0x86d9,0x86db,0x86e4,0x86ee,0x86f9,0x86fe,0x8700,
0x8702,0x8708,0x8712,0x8713,0x8715,0x8717,0x8718,0x871c,
0x8721,0x873b,0x8747,0x8749,0x874c,0x874e,0x8757,0x8759,
0x8760,0x8774,0x8776,0x8783,0x878d,0x879f,0x87ba,0x87c0,
0x87c6,0x87cb,0x87f9,0x8815,0x8822,0x8840,0x8845,0x884c,
0x884d,0x8854,0x8857,0x8859,0x8861,0x8863,0x8865,0x8868,
0x8869,0x886b,0x886c,0x8870,0x8877,0x8881,0x8884,0x888b,
0x888d,0x8892,0x8896,0x889c,0x88ab,0x88ad,0x88b1,0x88c1,
0x88c2,0x88c5,0x88c6,0x88c9,0x88d5,0x88d9,0x88e4,0x88f3,
0x88f8,0x88f9,0x8902,0x8910,0x8912,0x8925,0x895f,0x897f,
0x8981,0x8986,0x89c1,0x89c2,0x89c4,0x89c5,0x89c6,0x89c8,
0x89c9,0x89d2,0x89e3,0x89e6,0x8a00,0x8a89,0x8a8a,0x8a93,
0x8b66,0x8b6c,0x8ba1,0x8ba2,0x8ba4,0x8ba5,0x8ba8,0x8ba9,
0x8bad,0x8bae,0x8baf,0x8bb0,0x8bb2,0x8bb3,0x8bb6,0x8bb8,
0x8bb9,0x8bba,0x8bbc,0x8bbd,0x8bbe,0x8bbf,0x8bc0,0x8bc1,
0x8bc4,0x8bc5,0x8bc6,0x8bc8,0x8bc9,0x8bca,0x8bcd,0x8bd1,
0x8bd5,0x8bd7,0x8bda,0x8bdd,0x8bde,0x8be1,0x8be2,0x8be5,
0x8be6,0x8beb,0x8bec,0x8bed,0x8bef,0x8bf1,0x8bf2,0x8bf4,
0x8bf5,0x8bf7,0x8bf8,0x8bfa,0x8bfb,0x8bfd,0x8bfe,0x8c01,
0x8c03,0x8c05,0x8c06,0x8c08,0x8c0a,0x8c0b,0x8c0d,0x8c0e,
0x8c10,0x8c12,0x8c13,0x8c1a,0x8c1c,0x8c22,0x8c23,0x8c24,
0x8c26,0x8c28,0x8c2c,0x8c2d,0x8c31,0x8c34,0x8c37,0x8c41,
0x8c46,0x8c4c,0x8c61,0x8c6a,0x8c6b,0x8c79,0x8c7a,0x8c8c,
0x8d1d,0x8d1e,0x8d1f,0x8d21,0x8d22,0x8d23,0x8d24,0x8d25,
0x8d26,0x8d27,0x8d27,0x8d28,0x8d29,0x8d2a,0x8d2b,0x8d2c,
0x8d2d,0x8d2e,0x8d2f,0x8d30,0x8d31,0x8d34,0x8d35,0x8d38,
0x8d39,0x8d3a,0x8d3c,0x8d3e,0x8d3f,0x8d41,0x8d42,0x8d43,
0x8d44,0x8d4a,0x8d4b,0x8d4c,0x8d4e,0x8d4f,0x8d50,0x8d54,
0x8d56,0x8d58,0x8d5a,0x8d5b,0x8d5e,0x8d60,0x8d61,0x8d62,
0x8d64,0x8d66,0x8d6b,0x8d70,0x8d74,0x8d75,0x8d76,0x8d77,
0x8d81,0x8d85,0x8d8a,0x8d8b,0x8d9f,0x8da3,0x8db3,0x8db4,
0x8dbe,0x8dc3,0x8dcb,0x8dcc,0x8dd1,0x8ddb,0x8ddd,0x8ddf,
0x8de8,0x8dea,0x8def,0x8df3,0x8df5,0x8df7,0x8dfa,0x8e0a,
0x8e0f,0x8e22,0x8e29,0x8e2a,0x8e31,0x8e42,0x8e44,0x8e48,
0x8e4b,0x8e66,0x8e6c,0x8e6d,0x8e72,0x8e81,0x8e8f,0x8eab,
0x8eac,0x8eaf,0x8eb2,0x8eba,0x8f66,0x8f67,0x8f68,0x8f69,
0x8f6c,0x8f6e,0x8f6f,0x8f70,0x8f74,0x8f7b,0x8f7d,0x8f7f,
0x8f83,0x8f85,0x8f86,0x8f88,0x8f89,0x8f90,0x8f91,0x8f93,
0x8f95,0x8f96,0x8f99,0x8f9b,0x8f9c,0x8f9e,0x8f9f,0x8fa3,
0x8fa8,0x8fa9,0x8fab,0x8fb0,0x8fb1,0x8fb9,0x8fbd,0x8fbe,
0x8fc1,0x8fc2,0x8fc4,0x8fc5,0x8fc7,0x8fc8,0x8fce,0x8fd0,
0x8fd1,0x8fd4,0x8fd8,0x8fd9,0x8fdb,0x8fdc,0x8fdd,0x8fde,
0x8fdf,0x8feb,0x8ff0,0x8ff7,0x8ff9,0x8ffd,0x9000,0x9001,
0x9002,0x9003,0x9006,0x9009,0x900a,0x900f,0x9010,0x9012,
0x9014,0x9017,0x901a,0x901b,0x901d,0x901e,0x901f,0x9020,
0x9022,0x902e,0x9038,0x903b,0x903c,0x903e,0x9042,0x9047,
0x904d,0x904f,0x9053,0x9057,0x9063,0x9065,0x906d,0x906e,
0x9075,0x907f,0x9080,0x9091,0x9093,0x90a2,0x90a3,0x90a6,
0x90aa,0x90ae,0x90bb,0x90c1,0x90ca,0x90ce,0x90d1,0x90e8,
0x90ed,0x90fd,0x9119,0x914c,0x914d,0x9152,0x9157,0x915d,
0x9163,0x9165,0x916a,0x916c,0x9171,0x9175,0x9177,0x9178,
0x917f,0x9187,0x9189,0x918b,0x9192,0x91c7,0x91ca,0x91cc,
0x91cd,0x91ce,0x91cf,0x91d1,0x9274,0x9488,0x9489,0x9493,
0x9499,0x949d,0x949e,0x949f,0x94a0,0x94a2,0x94a5,0x94a6,
0x94a7,0x94a9,0x94ae,0x94b1,0x94b3,0x94bb,0x94be,0x94c1,
0x94c3,0x94c5,0x94c6,0x94d0,0x94db,0x94dc,0x94dd,0x94e1,
0x94e3,0x94ed,0x94f2,0x94f6,0x94f8,0x94fa,0x94fe,0x9500,
0x9501,0x9504,0x9505,0x9508,0x9509,0x950b,0x950c,0x9510,
0x9519,0x951a,0x9521,0x9523,0x9524,0x9525,0x9526,0x9528,
0x952d,0x952e,0x952f,0x9530,0x9539,0x953b,0x9540,0x9547,
0x954a,0x9550,0x955c,0x9563,0x9570,0x9576,0x957f,0x95e8,
0x95ea,0x95ed,0x95ee,0x95ef,0x95f0,0x95f2,0x95f4,0x95f7,
0x95f8,0x95f9,0x95fa,0x95fb,0x95fd,0x9600,0x9601,0x9605,
0x960e,0x9610,0x9614,0x961f,0x9631,0x9632,0x9633,0x9634,
0x9635,0x9636,0x963b,0x963f,0x9644,0x9645,0x9646,0x9648,
0x964b,0x964c,0x964d,0x9650,0x9655,0x9661,0x9662,0x9664,
0x9668,0x9669,0x966a,0x9675,0x9676,0x9677,0x9685,0x9686,
0x968f,0x9690,0x9694,0x9698,0x9699,0x969c,0x96a7,0x96b6,
0x96be,0x96c0,0x96c1,0x96c4,0x96c5,0x96c6,0x96c7,0x96cc,
0x96cf,0x96d5,0x96e8,0x96ea,0x96f3,0x96f6,0x96f7,0x96f9,
0x96fe,0x9700,0x9707,0x9709,0x970d,0x970e,0x971c,0x971e,
0x9732,0x9738,0x9739,0x9752,0x9756,0x9759,0x975e,0x9760,
0x9761,0x9762,0x9769,0x9774,0x9776,0x978b,0x978d,0x97a0,
0x97ad,0x97e7,0x97e9,0x97ed,0x97f3,0x97f5,0x9875,0x9876,
0x9877,0x9879,0x987a,0x987b,0x987d,0x987e,0x987f,0x9881,
0x9882,0x9884,0x9885,0x9886,0x9887,0x9888,0x988a,0x9891,
0x9893,0x9896,0x9897,0x9898,0x989c,0x989d,0x98a0,0x98a4,
0x98ce,0x98d2,0x98d8,0x98de,0x98df,0x9910,0x9965,0x996d,
0x996e,0x9970,0x9971,0x9972,0x9975,0x9976,0x997a,0x997c,
0x997f,0x9981,0x9985,0x9986,0x998b,0x998d,0x998f,0x9992,
0x9996,0x9999,0x9a6c,0x9a6e,0x9a6f,0x9a70,0x9a71,0x9a73,
0x9a74,0x9a76,0x9a79,0x9a7b,0x9a7c,0x9a7e,0x9a82,0x9a84,
0x9a86,0x9a87,0x9a8c,0x9a8f,0x9a91,0x9a97,0x9a9a,0x9aa1,
0x9aa4,0x9aa8,0x9ad3,0x9ad8,0x9b13,0x9b3c,0x9b41,0x9b42,
0x9b44,0x9b4f,0x9b54,0x9c7c,0x9c81,0x9c9c,0x9ca4,0x9cab,
0x9cb8,0x9cc4,0x9ccd,0x9cd6,0x9cde,0x9e1f,0x9e20,0x9e21,
0x9e23,0x9e25,0x9e26,0x9e2d,0x9e2f,0x9e33,0x9e35,0x9e3d,
0x9e3f,0x9e43,0x9e45,0x9e49,0x9e4a,0x9e4f,0x9e64,0x9e66,
0x9e70,0x9e7f,0x9ea6,0x9eb8,0x9ebb,0x9ec4,0x9ecd,0x9ece,
0x9ed1,0x9ed4,0x9ed8,0x9f0e,0x9f13,0x9f20,0x9f3b,0x9f50,
0x9f7f,0x9f84,0x9f99,0x9f9f]

def Unicode():
    val1 = random.choice(chinses)
    val2 = random.choice(chinses)
    return chr(val1)+chr(val2)



#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# def my_get_letter_list():
#     import re
#
#     fonts_range = []
#     for lines in file('Chinese_Range', 'r'):
#         fonts_range.extend(map(lambda x: int(x, 16), \
#             re.split(',',lines.strip().strip(','))))
#
#     letter_list = ''.join(unichr(yf) for yf in fonts_range)
#     return letter_list
