from time import sleep

for i in range(10):
    sample = open('samplefile.txt', 'a')
    print("I am scheduler")
    sample.write("I am scheduler")
    sample.flush()
    sample.close()
    sleep(1)
