# How to solve segmentation fault on VCS which is run without -full64 option

## Problem

### segfault in VCS R-2020.12-SP1
```bash
Command line: ./simv

--- Stack trace follows:

Dumping VCS Annotated Stack:
#0  0xf7ffd430 in __kernel_vsyscall ()
#1  0x006d569b in waitpid () from /lib/libc.so.6
#2  0x0066ebe3 in do_system () from /lib/libc.so.6
#3  0x0066ef72 in system () from /lib/libc.so.6
#4  0x007db9ed in system () from /lib/libpthread.so.0
#5  0xee4a66ec in SNPSle_10ee25eff68cd8461c9146fa1d0b35e87067f3c8015b313e639d2928478c79b3f673f99203bcf8be64600612100082236bffb2007f1e0ef9 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/liberrorinf.so
#6  0xee4a795b in SNPSle_10ee25eff68cd8461c9146fa1d0b35e87067f3c8015b313efba706aab251478fa49e66610e453774633a6c152e7ef778f2202cda681f3d4e () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/liberrorinf.so
#7  0xee49fd5b in SNPSle_d35ca1ff70d465c2b9b1a72eee90a50630165806651fae9621672f4baea6f56e () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/liberrorinf.so
#8  0xea2beb40 in SNPSle_64133461705005bb725549e2e6fa1b3f () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#9  0xe9f6c74c in SNPSle_82244d58c54c18c70d63edc9becab634 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#11 0xee448195 in mem_free () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libsnpsmalloc.so
#12 0xee420bc4 in snpsFreeFunc () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libsnpsmalloc.so
#13 0xe9ce58ee in SNPSle_edfd0437dc1f3ca1 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#14 0xe9ce631d in SNPSle_e2e2cbb6d2283a4d () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#15 0xe9ce40ad in SNPSle_382d0af7df412362 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#16 0xe9ce4636 in SNPSle_59279f7c9b103b1e () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#17 0xe9ce4776 in SNPSle_207fb97ffa75eca3 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#18 0x007d3bc9 in start_thread () from /lib/libpthread.so.0
#19 0x0071711e in clone () from /lib/libc.so.6
#0  0xf7ffd430 in __kernel_vsyscall ()
#1  0x006d5b86 in nanosleep () from /lib/libc.so.6
#2  0x006d59b0 in sleep () from /lib/libc.so.6
#3  0xe9a93da9 in SNPSle_95ae9cc2e78cc668673c60b8d88c4908 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#4  0xe9a93f17 in SNPSle_92de4d0d4cf0d6931bc37e8d42a01d93 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#5  0xe9a921b7 in SNPSle_b76ef993ee82b3d58a5cadddbec8b67c () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#6  0xe9a92528 in SNPSle_f28f24b8c84ac8f6e02e0b03bcd33aa8 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#7  0xe9a7be98 in SNPSle_5e54eaa1df739f6ed4c1ff24a0986ee6 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#8  0xe9a7c0c3 in SNPSle_058778405d2a6c04ddd18247ba7f440f () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#9  0xe9a7dabd in SNPSle_e376be325e61b493d6bd988d8077bacc () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#10 0xe9a7e742 in SNPSle_a10369bdf7c5916ddd6866ce7e2e861c () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#11 0xe9a81cad in SNPSle_00b1acee80c770570cd75f9efbe24cca () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#12 0xe9a77e9d in SNPSle_ba11b1edbd04051f5bb81b1861cdf84a () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#13 0xe9a67573 in SNPSle_2e65c0794628fc5af60953149776c29b () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#14 0xe9a63b74 in SNPSle_541f757be362289a7c9e5618c0ff28327846f8d3cc02839f () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#15 0xe9a647e9 in SNPSle_541f757be362289a7c9e5618c0ff283244765933a2ab0071 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#16 0xe9a5dc62 in SNPSle_c0de1345d5ab80930e06dd2b68f214c3 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#17 0xe9a5de3e in SNPSle_25cd5712eacded5ff943afa9a81fcb09 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#18 0xe9a5e1bc in SNPSle_25cd5712eacded5feaee03dc3430943e () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#19 0xe9a5e8e9 in SNPSle_541f757be362289a7c9e5618c0ff28323e4fa62265ee8f28 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#20 0xea2e0042 in SNPSle_490598bfebcc8e8183ad3550288b1f82 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#21 0xea2ebac4 in SNPSle_490598bfebcc8e81 () from /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
#22 0x0805cdd7 in main ()

Process VmPeak: 553656 kb, VmSize: 421564 kb
System Free Memory: 2006344 kb, System Free Swap: 16657512 kb
```

## Solution

### Let's get objdump
```bash
$ objdump -D /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so &> dump
```  
VIM allows to open big dump file. After opening find - **SNPSle_207fb97ffa75eca3**  
```
019e273a <SNPSle_207fb97ffa75eca3>:
 19e273a:   55                      push   %ebp
 19e273b:   31 c0                   xor    %eax,%eax
 19e273d:   89 e5                   mov    %esp,%ebp
 19e273f:   56                      push   %esi
 19e2740:   8b 75 08                mov    0x8(%ebp),%esi
 19e2743:   53                      push   %ebx
 19e2744:   e8 c6 14 5c 02          call   3fa3c0f <SNPSle_715314d83d0f61da9168d7348e45a64b3af050ec97b0cd6b>
 19e2749:   81 c3 b7 58 28 04       add    $0x42858b7,%ebx
 19e274f:   85 f6                   test   %esi,%esi
 19e2751:   74 1a                   je     19e276d <SNPSle_207fb97ffa75eca3+0x33>
 19e2753:   8b 06                   mov    (%esi),%eax
 19e2755:   85 c0                   test   %eax,%eax
 19e2757:   74 63                   je     19e27bc <SNPSle_207fb97ffa75eca3+0x82>
 19e2759:   69 c0 40 42 0f 00       imul   $0xf4240,%eax,%eax
 19e275f:   83 ec 0c                sub    $0xc,%esp
 19e2762:   50                      push   %eax
 19e2763:   e8 28 03 55 ff          call   f32a90 <usleep@plt>
 19e2768:   83 c4 10                add    $0x10,%esp
 19e276b:   eb 4f                   jmp    19e27bc <SNPSle_207fb97ffa75eca3+0x82>
 19e276d:   83 ec 0c                sub    $0xc,%esp
 19e2770:   50                      push   %eax
 19e2771:   e8 b0 fd ff ff          call   19e2526 <SNPSle_59279f7c9b103b1e>
 19e2776:   83 c4 10                add    $0x10,%esp
 19e2779:   48                      dec    %eax
 19e277a:   8b 83 70 f6 ff ff       mov    -0x990(%ebx),%eax
 19e2780:   75 09                   jne    19e278b <SNPSle_207fb97ffa75eca3+0x51>
 19e2782:   c7 40 64 02 00 00 00    movl   $0x2,0x64(%eax)
```  
We are interested in line - 19e2771:   **e8 b0 fd ff ff**          call   19e2526 <SNPSle_59279f7c9b103b1e>  
It's callq instruction which we can replace by some nop instructions.  
Nop instruction is **0x90** in hex code.

**First of all you must make backup of VCS tool!**

### Edit binary file via hexedit
```bash
$ hexedit /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so
```  
Find **e8 b0 fd ff ff** which is at **19e2771** address. And replace this bytes by 0x90! Save changes and close library.  
So let's check result via objdump:  
```bash
$ objdump -D /eda/SYNOPSYS/vcs/R-2020.12-SP1/linux/lib/libvcsnew.so &> new_dump
```  

```bash
019e273a <SNPSle_207fb97ffa75eca3>:
 19e273a:   55                      push   %ebp
 19e273b:   31 c0                   xor    %eax,%eax
 19e273d:   89 e5                   mov    %esp,%ebp
 19e273f:   56                      push   %esi
 19e2740:   8b 75 08                mov    0x8(%ebp),%esi
 19e2743:   53                      push   %ebx
 19e2744:   e8 c6 14 5c 02          call   3fa3c0f <SNPSle_715314d83d0f61da9168d7348e45a64b3af050ec97b0cd6b>
 19e2749:   81 c3 b7 58 28 04       add    $0x42858b7,%ebx
 19e274f:   85 f6                   test   %esi,%esi
 19e2751:   74 1a                   je     19e276d <SNPSle_207fb97ffa75eca3+0x33>
 19e2753:   8b 06                   mov    (%esi),%eax
 19e2755:   85 c0                   test   %eax,%eax
 19e2757:   74 63                   je     19e27bc <SNPSle_207fb97ffa75eca3+0x82>
 19e2759:   69 c0 40 42 0f 00       imul   $0xf4240,%eax,%eax
 19e275f:   83 ec 0c                sub    $0xc,%esp
 19e2762:   50                      push   %eax
 19e2763:   e8 28 03 55 ff          call   f32a90 <usleep@plt>
 19e2768:   83 c4 10                add    $0x10,%esp
 19e276b:   eb 4f                   jmp    19e27bc <SNPSle_207fb97ffa75eca3+0x82>
 19e276d:   83 ec 0c                sub    $0xc,%esp
 19e2770:   50                      push   %eax
 19e2771:   90                      nop
 19e2772:   90                      nop
 19e2773:   90                      nop
 19e2774:   90                      nop
 19e2775:   90                      nop
 19e2776:   83 c4 10                add    $0x10,%esp
 19e2779:   48                      dec    %eax
 19e277a:   8b 83 70 f6 ff ff       mov    -0x990(%ebx),%eax
 19e2780:   75 09                   jne    19e278b <SNPSle_207fb97ffa75eca3+0x51>
 19e2782:   c7 40 64 02 00 00 00    movl   $0x2,0x64(%eax)
``` 
