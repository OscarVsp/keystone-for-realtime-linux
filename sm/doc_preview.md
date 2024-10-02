#

Starting point -> [sm.c](src/sm.c)

ecall_handler for keystone sm -> [sm-sbi-opensbi](src/sm-sbi-opensbi.c)

Trap is added in [trap.S](src/trap.S) and link into [sbi_trap_hack.c](src/sbi_trap_hack.c) to handle interrupt for **IRQ_M_TIMER** and **IRQ_M_SOFT** `mcause`