/* 
This rule only detects Decoy Dog. It was adapted from Florian Roth Pupy_RAT Rule 
original author : Florian Roth / @neo23x0
original link : https://github.com/Neo23x0/signature-base/blob/master/yara/gen_pupy_rat.yar
*/

/* Rule Set ----------------------------------------------------------------- */


import "elf"
import "pe"

rule DecoyDog_Backdoor {
   meta:
  	description = "Detects Decoy Dog backdoor"
  	license = "Detection Rule License 1.1 https://github.com/Neo23x0/signature-base/blob/master/LICENSE"
  	author = "Infoblox Inc."
  	reference = "https://github.com/n1nj4sec/pupy-binaries"
  	date = "2023-07-11"

   strings:
  	$x1 = "reflectively inject a dll into a process." fullword ascii
  	$x2 = "ld_preload_inject_dll(cmdline, dll_buffer, hook_exit) -> pid" fullword ascii
  	$x3 = "LD_PRELOAD=%s HOOK_EXIT=%d CLEANUP=%d exec %s 1>/dev/null 2>/dev/null" fullword ascii
  	$x4 = "reflective_inject_dll" fullword ascii
  	$x5 = "ld_preload_inject_dll" fullword ascii
  	$x6 = "get_pupy_config() -> string" fullword ascii
  	$x7 = "[INJECT] inject_dll. OpenProcess failed." fullword ascii
  	$x8 = "reflective_inject_dll" fullword ascii
  	$x9 = "reflective_inject_dll(pid, dll_buffer, isRemoteProcess64bits)" fullword ascii
  	$x10 = "linux_inject_main" fullword ascii
  	$x11 = "jvm.PreferredClassLoader" fullword ascii
  	$x12 = "jvm.JNIEnv capsule is invalid" fullword ascii

   condition:
  	(3 of them and $x11 ) or (3 of them and $x12)
  	or (uint16(0) == 0x5a4d and pe.imphash() == "84a69bce2ff6d9f866b7ae63bd70b163" and $x11) or (elf.telfhash() == "t1fde0f101c9395f39ecd16430b41041a59107c73c904087309fb8d0e8d87e0077129f3f")
}
