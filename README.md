# How to solve segmentation fault on VCS

## Problem

### segfault in VCS_vQ-2020.03
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

## Solution

### At first use GDB
```bash
$ gdb ./simv
GNU gdb (GDB) Red Hat Enterprise Linux 7.6.1-120.el7
Copyright (C) 2013 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /test/run/simv...(no debugging symbols found)...done.
(gdb)
```  
Running of Debugging:  
```bash
(gdb) run
Starting program: /test/run/./simv 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
process 8968 is executing new program: /test/run/simv
Missing separate debuginfos, use: debuginfo-install glibc-2.17-325.el7_9.x86_64 libgcc-4.8.5-44.el7.x86_64 libstdc++-4.8.5-44.el7.x86_64 libxml2-2.9.1-6.el7.5.x86_64 numactl-libs-2.0.12-5.el7.x86_64 xz-libs-5.2.2-1.el7.x86_64 zlib-1.2.7-19.el7_9.x86_64
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib64/libthread_db.so.1".
Notice: timing checks disabled with +notimingcheck at compile-time
[New Thread 0x2aaada311700 (LWP 9007)]
[Thread 0x2aaada311700 (LWP 9007) exited]
[New Thread 0x2aaada311700 (LWP 9014)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x2aaada311700 (LWP 9014)]
0x00002aaacb911904 in mem_free () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libsnpsmalloc.so
Missing separate debuginfos, use: debuginfo-install bzip2-libs-1.0.6-13.el7.x86_64 dbus-glib-0.100-7.el7.x86_64 dbus-libs-1.10.24-15.el7.x86_64 elfutils-libelf-0.176-5.el7.x86_64 elfutils-libs-0.176-5.el7.x86_64 glib2-2.56.1-8.el7.x86_64 glibc-2.17-325.el7_9.x86_64 libattr-2.4.46-13.el7.x86_64 libblkid-2.23.2-65.el7_9.1.x86_64 libcap-2.22-11.el7.x86_64 libffi-3.0.13-19.el7.x86_64 libgcc-4.8.5-44.el7.x86_64 libgcrypt-1.5.3-14.el7.x86_64 libgpg-error-1.12-3.el7.x86_64 libmount-2.23.2-65.el7_9.1.x86_64 libselinux-2.5-15.el7.x86_64 libstdc++-4.8.5-44.el7.x86_64 libuuid-2.23.2-65.el7_9.1.x86_64 libxml2-2.9.1-6.el7.5.x86_64 lz4-1.8.3-1.el7.x86_64 numactl-libs-2.0.12-5.el7.x86_64 pcre-8.32-17.el7.x86_64 systemd-libs-219-78.el7_9.3.x86_64 xz-libs-5.2.2-1.el7.x86_64 zlib-1.2.7-19.el7_9.x86_64
(gdb)
```  
So we get segfault which should be fixed. To do it we need to get backtrace:  
```bash
(gdb) backtrace 
#0  0x00002aaacb911904 in mem_free () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libsnpsmalloc.so
#1  0x00002aaacb8ed015 in snpsCheckFreeFunc () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libsnpsmalloc.so
#2  0x00002aaacd8428f4 in SNPSle_540905a7b1b27611 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#3  0x00002aaacd84323a in SNPSle_9ff9b2dce8f1fde9 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#4  0x00002aaacd841308 in SNPSle_36c2d46996c96605 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#5  0x00002aaacd8417cd in SNPSle_2c2186f0f2f42415 () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#6  0x00002aaacd8418e3 in SNPSle_126d17af453e054a () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
#7  0x00002aaad2ca3ea5 in start_thread () from /lib64/libpthread.so.0
#8  0x00002aaad35c0b0d in clone () from /lib64/libc.so.6
(gdb)
```  
Attention on GDB frame 6  
```bash
(gdb) frame 6
#6  0x00002aaacd8418e3 in SNPSle_126d17af453e054a () from /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
(gdb) disas
Dump of assembler code for function SNPSle_126d17af453e054a:
   0x00002aaacd8418c0 <+0>:	push   %rbx
   0x00002aaacd8418c1 <+1>:	mov    %rdi,%rbx
   0x00002aaacd8418c4 <+4>:	xor    %edi,%edi
   0x00002aaacd8418c6 <+6>:	test   %rbx,%rbx
   0x00002aaacd8418c9 <+9>:	je     0x2aaacd8418de <SNPSle_126d17af453e054a+30>
   0x00002aaacd8418cb <+11>:	mov    (%rbx),%eax
   0x00002aaacd8418cd <+13>:	test   %eax,%eax
   0x00002aaacd8418cf <+15>:	je     0x2aaacd841930 <SNPSle_126d17af453e054a+112>
   0x00002aaacd8418d1 <+17>:	imul   $0xf4240,%eax,%edi
   0x00002aaacd8418d7 <+23>:	callq  0x2aaacce069c0 <usleep@plt>
   0x00002aaacd8418dc <+28>:	jmp    0x2aaacd841930 <SNPSle_126d17af453e054a+112>
   0x00002aaacd8418de <+30>:	callq  0x2aaacd8416d6 <SNPSle_2c2186f0f2f42415>
=> 0x00002aaacd8418e3 <+35>:	dec    %eax
   0x00002aaacd8418e5 <+37>:	lea    0x3b55614(%rip),%rax        # 0x2aaad1396f00
   0x00002aaacd8418ec <+44>:	jne    0x2aaacd8418fa <SNPSle_126d17af453e054a+58>
   0x00002aaacd8418ee <+46>:	movl   $0x2,0x88(%rax)
```  
As you can see **SNPSle_2c2186f0f2f42415** doesn't have return data. So I suppose we can ignore calling of this function.

### Let's get objdump
```bash
$ objdump -D /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so &> dump
```  
VIM allows to open big dump file. After opening find - **SNPSle_126d17af453e054a**  
```bash

0000000001aaf8c0 <SNPSle_126d17af453e054a>:
 1aaf8c0:   53                      push   %rbx
 1aaf8c1:   48 89 fb                mov    %rdi,%rbx
 1aaf8c4:   31 ff                   xor    %edi,%edi
 1aaf8c6:   48 85 db                test   %rbx,%rbx
 1aaf8c9:   74 13                   je     1aaf8de <SNPSle_126d17af453e054a+0x1e>
 1aaf8cb:   8b 03                   mov    (%rbx),%eax
 1aaf8cd:   85 c0                   test   %eax,%eax
 1aaf8cf:   74 5f                   je     1aaf930 <SNPSle_126d17af453e054a+0x70>
 1aaf8d1:   69 f8 40 42 0f 00       imul   $0xf4240,%eax,%edi
 1aaf8d7:   e8 e4 50 5c ff          callq  10749c0 <usleep@plt>
 1aaf8dc:   eb 52                   jmp    1aaf930 <SNPSle_126d17af453e054a+0x70>
 1aaf8de:   e8 f3 fd ff ff          callq  1aaf6d6 <SNPSle_2c2186f0f2f42415>
 1aaf8e3:   ff c8                   dec    %eax
 1aaf8e5:   48 8d 05 14 56 b5 03    lea    0x3b55614(%rip),%rax        # 5604f00 <.got+0x15808>
```  
We are interested in line - 1aaf8de:   **e8 f3 fd ff ff**          callq  1aaf6d6 <SNPSle_2c2186f0f2f42415>  
It's callq instruction which we can replace by some nop instructions.  
Nop instruction is **0x90** in hex code.

**First of all you must make backup of VCS tool!**

### Edit binary file via hexedit
```bash
$ hexedit /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so
```  
Find **e8 f3 fd ff ff** which is at **1aaf8de** address. And replace this bytes by 0x90! Save changes and close library.  
So let's check result via objdump:  
```bash
$ objdump -D /eda/synopsys/vcs/Q-2020.03/linux64/lib/libvcsnew.so &> new_dump
```  
go to **1aaf8de**  
```bash

0000000001aaf8c0 <SNPSle_126d17af453e054a>:
 1aaf8c0:   53                      push   %rbx
 1aaf8c1:   48 89 fb                mov    %rdi,%rbx
 1aaf8c4:   31 ff                   xor    %edi,%edi
 1aaf8c6:   48 85 db                test   %rbx,%rbx
 1aaf8c9:   74 13                   je     1aaf8de <SNPSle_126d17af453e054a+0x1e>
 1aaf8cb:   8b 03                   mov    (%rbx),%eax
 1aaf8cd:   85 c0                   test   %eax,%eax
 1aaf8cf:   74 5f                   je     1aaf930 <SNPSle_126d17af453e054a+0x70>
 1aaf8d1:   69 f8 40 42 0f 00       imul   $0xf4240,%eax,%edi
 1aaf8d7:   e8 e4 50 5c ff          callq  10749c0 <usleep@plt>
 1aaf8dc:   eb 52                   jmp    1aaf930 <SNPSle_126d17af453e054a+0x70>
 1aaf8de:   90                      nop
 1aaf8df:   90                      nop
 1aaf8e0:   90                      nop
 1aaf8e1:   90                      nop
 1aaf8e2:   90                      nop
 1aaf8e3:   ff c8                   dec    %eax
 1aaf8e5:   48 8d 05 14 56 b5 03    lea    0x3b55614(%rip),%rax        # 5604f00 <.got+0x15808>
```

### Test
```bash
$ ./simv
...

$finish called from file "/eda/synopsys/vcs/Q-2020.03//etc/uvm-1.2/base/uvm_root.svh", line 613.
$finish at simulation time 0.000ns
           V C S   S i m u l a t i o n   R e p o r t 
Time: 0 ps
CPU Time:      2.420 seconds;       Data structure size:  11.7Mb
Sun Mar 20 09:31:25 2022
```  
As you see we done it! We aren't facing segmentation fault!
