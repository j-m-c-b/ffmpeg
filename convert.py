import subprocess

def videoToAudio():
    videoFN = input("Video File name: ")
    audioFN = input("New audio File Name (with extension): ")
    
    answer = input("You wish to give give a beginning and a end  in seconds (Y/n)?: ")
    
    if answer.lower() == "y":
        begin = input("Starts at? (seconds): ")
        end = input("Ends at? (seconds): ")

        duration = str(float(end) - float(begin))


        subprocess.run(["ffmpeg", "-i", videoFN, "-ss", begin
        , "-t", duration,  "-q:a", "0" 
        , "-map", "a", audioFN])

    else:
        subprocess.run(["ffmpeg", "-i", videoFN, "-q:a", "0" 
        , "-map", "a", audioFN])


def extractVideoPart():
    videoFN = input("Video file name: ")
    newVideoFN = input("NEW video part file name: ")
    begin = input("Starts at? (seconds): ")
    end = input("Ends at? (seconds): ")

    duration = str(float(end) - float(begin))

    subprocess.run(["ffmpeg", "-i", videoFN, "-ss", begin
        , "-t", duration,  "-c", "copy" 
        , newVideoFN])
 
  

options = ["Video to audio", "Extract a part of a video"]


for index, option in enumerate(options):
    print(str(index+1) + ".", option)


choice = int(input("Please select one option: "))
if choice == 1:
        videoToAudio()
elif choice == 2:
        extractVideoPart()