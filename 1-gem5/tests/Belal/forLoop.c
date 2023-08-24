
int main(int argc, char* argv[])
{
    asm volatile("" ::: "memory");
    for(int i=0; i<100; ++i)
    	asm("nop");
    
    return 0;
}

