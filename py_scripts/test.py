
def main():
    i = 0
    while True:
        print(i)
        i+=1
#will run forever

if __name__=="__main__":
    main()

#ctr+z = pause 
#fg = whetever has been paused in the background push it to forreground (obs app has to stay open)
#tmux new -s counter = create tmux session
#ct+b+d = detatch from session
#tmux ls 
# tmux a -t counter = attack to session again