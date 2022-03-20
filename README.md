## It shows how to solve segmentation fault on VCS

### Problem

#### segfault in VCS_vQ-2020.03
```bash
Command line: ./simv

--- Stack trace follows:

Dumping VCS Annotated Stack:
#0  0x00002aaad3587659 in waitpid () from /lib64/libc.so.6
#1  0x00002aaad3504f62 in do_system () from /lib64/libc.so.6
#2  0x00002aaad3505311 in system () from /lib64/libc.so.6
#3  0x00002aaacb5883fb in SNPSle_10ee25eff68cd8461c9146fa1d0b35e87067f3c8015b313e639d2928478c79b3f673f99203bcf8be64600612100082236bffb2007f1e0ef9 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/liberrorinf.so
#4  0x00002aaacb589ed3 in SNPSle_10ee25eff68cd8461c9146fa1d0b35e87067f3c8015b313efba706aab251478fa49e66610e453774633a6c152e7ef778f2202cda681f3d4e () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/liberrorinf.so
#5  0x00002aaacb582822 in SNPSle_d35ca1ff70d465c2b9b1a72eee90a50630165806651fae96eee2bdb18305df1f () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/liberrorinf.so
#6  0x00002aaacdd162af in SNPSle_64133461705005bb725549e2e6fa1b3f () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#7  0x00002aaacda6fbef in SNPSle_82244d58c54c18c70d63edc9becab634 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#9  0x00002aaacb911904 in mem_free () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libsnpsmalloc.so
#10 0x00002aaacb8ed015 in snpsCheckFreeFunc () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libsnpsmalloc.so
#11 0x00002aaacd8428f4 in SNPSle_540905a7b1b27611 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#12 0x00002aaacd84323a in SNPSle_9ff9b2dce8f1fde9 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#13 0x00002aaacd841308 in SNPSle_36c2d46996c96605 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#14 0x00002aaacd8417cd in SNPSle_2c2186f0f2f42415 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#15 0x00002aaacd8418e3 in SNPSle_126d17af453e054a () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#16 0x00002aaad2ca3ea5 in start_thread () from /lib64/libpthread.so.0
#17 0x00002aaad35c0b0d in clone () from /lib64/libc.so.6
#0  0x00002aaad35879fd in nanosleep () from /lib64/libc.so.6
#1  0x00002aaad3587894 in sleep () from /lib64/libc.so.6
#2  0x00002aaacd5e1b76 in SNPSle_95ae9cc2e78cc668673c60b8d88c4908 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#3  0x00002aaacd5e1d19 in SNPSle_92de4d0d4cf0d6931bc37e8d42a01d93 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#4  0x00002aaacd5e008a in SNPSle_b76ef993ee82b3d58a5cadddbec8b67c () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#5  0x00002aaacd5e032c in SNPSle_f28f24b8c84ac8f6e02e0b03bcd33aa8 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#6  0x00002aaacd5cba31 in SNPSle_5e54eaa1df739f6ed4c1ff24a0986ee6 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#7  0x00002aaacd5cbc4c in SNPSle_058778405d2a6c04ddd18247ba7f440f () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#8  0x00002aaacd5c67d2 in SNPSle_e376be325e61b493d6bd988d8077bacc () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#9  0x00002aaacd5c6c0f in SNPSle_a10369bdf7c5916ddd6866ce7e2e861c () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#10 0x00002aaacd5c73e1 in SNPSle_00b1acee80c770570cd75f9efbe24cca () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#11 0x00002aaacd5c7e6d in SNPSle_ba11b1edbd04051f5bb81b1861cdf84a () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#12 0x00002aaacd5b6602 in SNPSle_2e65c0794628fc5af60953149776c29b () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#13 0x00002aaacd5b3262 in SNPSle_541f757be362289a7c9e5618c0ff28327846f8d3cc02839f () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#14 0x00002aaacd5ad08a in SNPSle_c0de1345d5ab80930e06dd2b68f214c3 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#15 0x00002aaacd5ad242 in SNPSle_25cd5712eacded5ff943afa9a81fcb09 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#16 0x00002aaacdd34da9 in SNPSle_490598bfebcc8e8183ad3550288b1f82 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#17 0x00002aaacdd41962 in SNPSle_490598bfebcc8e81 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#18 0x00000000004171ff in main ()

Process VmPeak: 916968 kb, VmSize: 851436 kb
System Free Memory: 119334916 kb, System Free Swap: 4194300 kb

```

### Solution

#### At first use GDB
```bash

```  
Attention on GDB frame 4

#### Next get dump via objdump

```bash

```

#### Then 
