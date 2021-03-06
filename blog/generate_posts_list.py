﻿#!/usr/bin/env python
import datetime, time, email.utils

def post(f_rss, f_html, TS, URL, title):

    full_URL="https://yurichev.com/blog/"+URL+"/"
    
    f_rss.write("    <item>\n")
    f_rss.write("      <title>"+title+"</title> \n")
    f_rss.write("      <link>"+full_URL+"</link> \n")
    f_rss.write("      <description>"+title+"</description> \n")
    f_rss.write("      <pubDate>"+email.utils.formatdate(time.mktime(TS.timetuple()), True)+"</pubDate>\n")
    f_rss.write("    </item>\n")

    f_html.write("<tr><td>"+TS.strftime("%d-%b-%Y") + "</td><td><a href=\""+ full_URL +"\">"+title+"</a></td></tr>\n")

def main():
    f1=open("rss.xml","w")
    f2=open("posts.html","w")

    f1.write ("<rss version=\"2.0\">\n")
    f1.write ("  <channel> \n")
    f1.write ("    <title>Dennis Yurichev</title> \n")
    f1.write ("    <link>https://yurichev.com/blog/</link> \n")
    f1.write ("    <description>by Dennis Yurichev</description>\n")

    f2.write ("<table>\n")

    post(f1,f2,datetime.datetime(2017, 2, 9,0,0,0), "symbolic","Symbolic execution")
    post(f1,f2,datetime.datetime(2017, 2, 7,0,0,0), "SAP","SAP cluster table unpacker")
    post(f1,f2,datetime.datetime(2017, 1,15,0,0,0), "pgm_synth","Simple program synthesis using Z3 SMT-solver")
    post(f1,f2,datetime.datetime(2016,12, 5,0,0,0), "farsi","\"Reverse Engineering for Beginners\" book in Farsi (Persian language)")
    post(f1,f2,datetime.datetime(2016,12, 5,0,0,0), "toy_decompiler","Toy decompiler for x86-64 written in Python")
    post(f1,f2,datetime.datetime(2016, 7,10,0,0,0), "loop_optimization","Another loop optimization") #
    post(f1,f2,datetime.datetime(2016, 6,29,0,0,0), "ptrs5","C/C++ pointers: array as function argument") #
    post(f1,f2,datetime.datetime(2016, 6,27,0,0,0), "bitcoin_miner","Overclocking Cointerra Bitcoin miner") #
    post(f1,f2,datetime.datetime(2016, 6,13,0,0,0), "ptrs4","C/C++ pointers: null pointers") #
    post(f1,f2,datetime.datetime(2016, 6, 2,0,0,0), "ptrs3","C/C++ pointers: pointers abuse in Windows kernel") #
    post(f1,f2,datetime.datetime(2016, 5,22,0,0,0), "ptrs2","C/C++ pointers: yet another abuse") #
    post(f1,f2,datetime.datetime(2016, 5,19,0,0,0), "weird_loop_optimization","Weird loop optimization") #
    post(f1,f2,datetime.datetime(2016, 5, 8,0,0,0), "ptrs","C/C++ pointers: yet another short example") #

    post(f1,f2,datetime.datetime(2016, 5, 6,0,0,0), "breaking_simple_exec_crypto","Breaking simple executable cryptor") #
    post(f1,f2,datetime.datetime(2016, 5, 6,0,0,0), "args_stat","Function arguments statistics") #
    post(f1,f2,datetime.datetime(2016, 5, 3,0,0,0), "XOR_mask_2","Simple encryption using XOR mask, part II") #
    post(f1,f2,datetime.datetime(2016, 4,29,0,0,0), "XOR_mask_1","Simple encryption using XOR mask") #
    post(f1,f2,datetime.datetime(2016, 4,22,0,0,0), "signed_division_using_shifts","Signed division using shifts")
    post(f1,f2,datetime.datetime(2016, 4,19,0,0,0), "lzhuf","Bug in LZHuf.c by Haruyasu Yoshizaki")
    post(f1,f2,datetime.datetime(2015,11,12,0,0,0), "challenges.re","My new website about reverse engineering challenges/exercises/problems/tasks: challenges.re")
    post(f1,f2,datetime.datetime(2015, 9,27,0,0,0), "git","Some of git internals")
    post(f1,f2,datetime.datetime(2015, 9,27,0,0,0), "CAS","Content-addressable storage")
    post(f1,f2,datetime.datetime(2015, 9, 8,0,0,0), "typeless","Typeless programming languages (BCPL, B), C evolution and decompiling")
    post(f1,f2,datetime.datetime(2015, 9, 4,0,0,0), "FAT12", "(Beginners level) packing 12-bit values into array using bit operations (x64, ARM/ARM64, MIPS)") #
    post(f1,f2,datetime.datetime(2015, 8,26,0,0,0), "2015-aug-26", "Yet another compiler anomaly") #
    post(f1,f2,datetime.datetime(2015, 8,26,0,0,0), "encrypted_DB_case_1", "Encrypted database case #1") #
    post(f1,f2,datetime.datetime(2015, 8,22,0,0,0), "de_bruijn", "De Bruijn sequences (solution for the exercise posted at 18-Aug-2015); leading/trailing zero bits counting.")
    post(f1,f2,datetime.datetime(2015, 8,20,0,0,0), "2015-aug-20", "Some parts of my Reverse Engineering book translated to Chinese.")

    post(f1,f2,datetime.datetime(2015, 8,13,0,0,0), "2015-aug-13", "Introduction to logarithms; yet another x86 reverse engineering exercise")
    post(f1,f2,datetime.datetime(2015, 7,23,0,0,0), "fuzzy_string", "Fuzzy string matching + simplest possible spellchecking + hunting for typos and misspellings in Wikipedia")
    post(f1,f2,datetime.datetime(2015, 7,22,0,0,0), "clique", "Clique in graph theory")
    post(f1,f2,datetime.datetime(2015, 7, 9,0,0,0), "RSA", "How RSA works")
    post(f1,f2,datetime.datetime(2015, 6,13,0,0,0), "modulo", "Modular arithmetic + division by multiplication + reversible LCG (PRNG) + cracking LCG with Z3")
    post(f1,f2,datetime.datetime(2015, 5,16,0,0,0), "llvm", "Tweaking LLVM Obfuscator + quick look into some of LLVM internals")
    post(f1,f2,datetime.datetime(2015, 5,13,0,0,0), "entropy", "(Beginners level) Analyzing unknown binary files using information entropy") #
    post(f1,f2,datetime.datetime(2015, 4,25,0,0,0), "fortune", "(Beginners level) reverse engineering of simple fortune program indexing file") #
    post(f1,f2,datetime.datetime(2015, 4,20,0,0,0), "86", "Using Z3 theorem prover to prove equivalence of some bizarre alternative to XOR operation.")
    post(f1,f2,datetime.datetime(2015, 1,21,0,0,0), "85", "Korean publication of \"Reverse Engineering for Beginners\" book is available for pre-order!")
    post(f1,f2,datetime.datetime(2014, 8,29,0,0,0), "84", "Publishers?")
    post(f1,f2,datetime.datetime(2014, 8, 8,0,0,0), "83", "\"Reverse Engineering for Beginners\" free book news")
    post(f1,f2,datetime.datetime(2014, 4, 9,0,0,0), "82", "Couple of win32 PE patching utilities")
    post(f1,f2,datetime.datetime(2014, 3,29,0,0,0), "81", "Cracking simple hash-function using Z3 SMT-solver")
    post(f1,f2,datetime.datetime(2014, 3, 5,0,0,0), "80", "My \"Reverse Engineering for Beginners\" book")
    post(f1,f2,datetime.datetime(2014, 2,18,0,0,0), "79", "PE add imports")
    post(f1,f2,datetime.datetime(2013,12,18,0,0,0), "77", "Convert to sparse file utility (win32)")
    post(f1,f2,datetime.datetime(2013,10,16,0,0,0), "76", "Add import to PE executable file")
    post(f1,f2,datetime.datetime(2013,10,15,0,0,0), "75", "New tracer features for software testing")
    post(f1,f2,datetime.datetime(2013, 8,19,0,0,0), "74", "Bug or typo or?..")
    post(f1,f2,datetime.datetime(2013, 7, 3,0,0,0), "73", "\"Quick introduction to reverse engineering for beginners\" book update")
    post(f1,f2,datetime.datetime(2013, 3,14,0,0,0), "72", "\"Quick introduction to reverse engineering for beginners\"")
    post(f1,f2,datetime.datetime(2012, 8,14,0,0,0), "71", "Finding unknown algorithm using only input/output pairs and Z3 SMT solver")
    post(f1,f2,datetime.datetime(2012, 7,19,0,0,0), "70", "Three PoCs from CPUjul2012")
    post(f1,f2,datetime.datetime(2012, 7,17,0,0,0), "69", "CVE-2012-0072 PoC (fixed in CPUjan2012)")
    post(f1,f2,datetime.datetime(2012, 7,17,0,0,0), "68", "CVE-2010-0911 PoC (fixed in CPUjul2010)")
    post(f1,f2,datetime.datetime(2011, 9,23,0,0,0), "66", "Extreme hardening by code modification.")
    post(f1,f2,datetime.datetime(2011, 7,27,0,0,0), "65", "Dataflow tracker")
    post(f1,f2,datetime.datetime(2011, 7,27,0,0,0), "64", "Strings in Oracle RDBMS network layer")
    post(f1,f2,datetime.datetime(2011, 4, 6,0,0,0), "61", "ops_SIMD 0.3")
    post(f1,f2,datetime.datetime(2011, 1,19,0,0,0), "60", "Oracle passwords (DES) solver updating to support AVX")
    post(f1,f2,datetime.datetime(2011, 1,14,0,0,0), "59", "Generic tracer 0.5 beta")
    post(f1,f2,datetime.datetime(2010,12, 7,0,0,0), "58", "Making C compiler generate obfuscated code")
    post(f1,f2,datetime.datetime(2010,11,24,0,0,0), "57", "Oracle .msb files unpacker")
    post(f1,f2,datetime.datetime(2010,10,31,0,0,0), "56", "Adding old dongle support to DosBox")
    post(f1,f2,datetime.datetime(2010,10,29,0,0,0), "55", "Using debugging features of DosBox")
    post(f1,f2,datetime.datetime(2010,10,10,0,0,0), "54", "Oracle passwords (DES) solver 0.2 (SSE2)")
    post(f1,f2,datetime.datetime(2010, 7,13,0,0,0), "52", "Tracing connection between TDW_NOCOMPRESS SAPGUI envrionment variable to bothering window and actual data compression routine")
    post(f1,f2,datetime.datetime(2010, 7,11,0,0,0), "51", "\"QR9\": Rubik's cube inspired amateur crypto-algorithm")
    post(f1,f2,datetime.datetime(2010, 7, 7,0,0,0), "50", "About Oracle PL/SQL undocumented \"interface\" pragma.")
    post(f1,f2,datetime.datetime(2010, 6, 7,0,0,0), "49", "SAP license + password checking functions...")
    post(f1,f2,datetime.datetime(2010, 6, 7,0,0,0), "48", "Generic tracer 0.4")
    post(f1,f2,datetime.datetime(2010, 6, 2,0,0,0), "47", "About SAP network packets decompressing and also SAP network password sniffing")
    post(f1,f2,datetime.datetime(2010, 5,24,0,0,0), "46", "PEEKs and POKEs in Windows x64?")
    post(f1,f2,datetime.datetime(2010, 4,15,0,0,0), "45", "My two oracle passwords crackers")
    post(f1,f2,datetime.datetime(2010, 3,12,0,0,0), "44", "SAP")
    post(f1,f2,datetime.datetime(2010, 2, 6,0,0,0), "43", "Oracle RDBMS internal self-testing features")
    post(f1,f2,datetime.datetime(2010, 1,30,0,0,0), "42", "Random Oracle hosts statistics")
    post(f1,f2,datetime.datetime(2010, 1,26,0,0,0), "41", "Rendering data structures passed to functions as arguments")
    post(f1,f2,datetime.datetime(2010, 1,22,0,0,0), "39", "Metasploit plugin based on CVE-2009-1979")
    post(f1,f2,datetime.datetime(2010, 1,22,0,0,0), "38", "CVE-2010-0071")
    post(f1,f2,datetime.datetime(2010, 1,20,0,0,0), "37", "My Oracle TNS Listener rootkit experiment")
    post(f1,f2,datetime.datetime(2010, 1,19,0,0,0), "36", "My Oracle rootkit experiment")
    post(f1,f2,datetime.datetime(2010, 1,15,0,0,0), "35", "More information about CVE-2009-1979 (CPUoct2009)")
    post(f1,f2,datetime.datetime(2009,12,24,0,0,0), "33", "Events checked in some major Oracle RDBMS versions")
    post(f1,f2,datetime.datetime(2009,12,24,0,0,0), "32", "Radiohead lyrics in Oracle RDBMS code")
    post(f1,f2,datetime.datetime(2009,12,22,0,0,0), "31", "Rare x86 instruction")
    post(f1,f2,datetime.datetime(2009,12, 6,0,0,0), "30", "FPGA-based Oracle RDBMS passwords solver")
    post(f1,f2,datetime.datetime(2009,12, 5,0,0,0), "29", "Generic tracer 0.3")
    post(f1,f2,datetime.datetime(2009,10,30,0,0,0), "28", "CVE-2009-1979 PoC (CPUoct2009)")
    post(f1,f2,datetime.datetime(2009,10, 5,0,0,0), "27", "Oracle RDBMS passwords solver")
    post(f1,f2,datetime.datetime(2009, 7,24,0,0,0), "26", "CVE-2009-1970 PoC (CPUjul2009)")
    post(f1,f2,datetime.datetime(2009, 7,24,0,0,0), "25", "CVE-2009-1963 PoC (CPUjul2009)")
    post(f1,f2,datetime.datetime(2009, 7,24,0,0,0), "24", "CVE-2009-1019 PoC (CPUjul2009)")
    post(f1,f2,datetime.datetime(2009, 7,24,0,0,0), "23", "CVE-2009-1020 PoC (CPUjul2009)")
    post(f1,f2,datetime.datetime(2009, 5,21,0,0,0), "22", "Generic tracer")
    post(f1,f2,datetime.datetime(2009, 4,21,0,0,0), "18", "CPUapr2009")
    post(f1,f2,datetime.datetime(2009, 4, 2,0,0,0), "17", "IBM DB2")
    post(f1,f2,datetime.datetime(2009, 1, 7,0,0,0), "15", "CHANGE USER OPI call")
    post(f1,f2,datetime.datetime(2008,11, 4,0,0,0), "14", "Oracle SPY Events")
    post(f1,f2,datetime.datetime(2008,10, 2,0,0,0), "13", "SYS_OP_*")
    post(f1,f2,datetime.datetime(2008, 9,29,0,0,0), "12", "Oracle RDBMS 11.1.0.7.0 some internals info")
    post(f1,f2,datetime.datetime(2008, 9,25,0,0,0), "11", "Basics of C within the Oracle kernel.")
    post(f1,f2,datetime.datetime(2008, 9, 4,0,0,0), "10", "Oracle internals")
    post(f1,f2,datetime.datetime(2008, 7,30,0,0,0), "9", "Oracle SPY")
    post(f1,f2,datetime.datetime(2008, 7,23,0,0,0), "8", "Intel(R) C++?")
    post(f1,f2,datetime.datetime(2008, 7,13,0,0,0), "7", "Network trace in Oracle RDBMS")
    post(f1,f2,datetime.datetime(2008, 7,13,0,0,0), "6", "malloc() comments")
    post(f1,f2,datetime.datetime(2008, 7,13,0,0,0), "5", "Solving Oracle passwords hashes using FPGA.")
    post(f1,f2,datetime.datetime(2008, 7,13,0,0,0), "4", "Evolution")
    post(f1,f2,datetime.datetime(2008, 7,10,0,0,0), "3", "_disable_txn_alert undocumented parameter in Oracle 11g")
    post(f1,f2,datetime.datetime(2008, 6,26,0,0,0), "2", "Oracle X$KSMLRU fixed table")
    post(f1,f2,datetime.datetime(2008, 2,17,0,0,0), "1", "Oracle V$TIMER")
    
    f2.write ("</table>\n")
 
    f1.write ("  </channel>\n")
    f1.write ("</rss>\n")
  
    f1.close()
    f2.close()

main()

