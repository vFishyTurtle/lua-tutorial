

## IGNORE MESSY CODE I WAS IN A RUSH






from colorama import Fore, Style, init
import os
import time

RED = Fore.RED
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
PINK = Fore.LIGHTMAGENTA_EX
CYAN = Fore.LIGHTBLUE_EX

print(f"Credits - vFishy")

print(f"Please fullscreen this window so you get the best learning experience.")

input(f"Welcome to lua for retards! Press enter to continue!")
os.system('cls' if os.name == 'nt' else 'clear')

# // wtf is lua

print(f"{BLUE}So basically in roblox exploiting, this is what you do.{RESET}")
print(f"1. Open Dark Dex")
print(f"2. Find a Path")
print(f"3. Fuck wit it")
print("\n(sometimes use rspy)")

time.sleep(2)
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

# // GetChildren and GetDescendants
print(f"{BLUE}First you need to know the damn difference bewtween a child and a descendant.{RESET}")
print(f"""
    workspace -- The parent
        Player1 -- Child of workspace
            HumanoidRootPart -- Descendant of Workspace but also can be a child of Player1
            Head -- Descendant of Workspace but also can be a child of Player1
            Torso -- Descendant of Workspace but also can be a child of Player1
            Football -- Descendant of Workspace but also can be a child of Player1
""")

print(f"\n\n{BLUE}Ok hopefully your dumbass understands cause if not you aint making jackshit with lua! Press Enter to continue!{RESET}")
input("")
os.system('cls' if os.name == 'nt' else 'clear')

# // For i, v in pairs
print(f"{BLUE}Ok now ima teach your ass how to do an index search or someshit. This is the main fucking thing you needa know ngl.{RESET}")
print("\nWhite = not important just know to type it")
print(f"{RED}Red = VERY FUCKING IMPORTANT HOLY SHIT{RESET}")
print(f"{GREEN}Green = somewhat important{RESET}")

print(f"""
    Here is an example of finding the football in football fusion 2
      
    for {GREEN}i{RESET}, {RED}v{RESET} in pairs({GREEN}game.workspace:GetChildren(){RESET}) do
        if {RED}v.Name == "Football"{RESET} and {RED}v:IsA("BasePart"){RESET} then
            {GREEN}print(v){RESET}
        end
    end\n
""")

time.sleep(2)

print(f"""
Now since i already know your ass didnt understand one bit let me break it down
      
      1. for {GREEN}i{RESET}, {RED}v{RESET} in pairs() | main thing you need to understand is that v is your value.
      2. {GREEN}game.workspace:GetChildren(){RESET} | This gets all children in the workspace
      3. {RED}v.Name == "Football"{RESET} and {RED}v:IsA("BasePart"){RESET} | Checks if the child is named football and is a part
      4. {GREEN}print(v){RESET} | Prints the value. (football)
      5. End | shit just means your done. I just add these when shit be erroring and i cba to debug\n\n
""")
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{BLUE}Now you wil learn how to use firetouchinterest!{RESET}")

print("\nExample of how to use | firetouchinterest(part you want to touch it, thing to touch, 0 or 1)")

print(f"""
Heres an example of it in use in a script
      
      for i, v in pairs(game.workspace.Orbs.OrbSpawns:GetChildren()) do
        if v.Name == "Orb" then
            firetouchinterest(game.Players.LocalPlayer.Character.Head, v, 0)
            task.wait()
            firetouchinterest(game.Players.LocalPlayer.Character.Head, v, 1)
        end
    end\n
""")
time.sleep(2)
print("""
Ok so i already know you dont understand this aswell so here is another break down
    
1. for i, v in pairs shit you learned earlier
2. firetouchinterest(game.Players.LocalPlayer.Character.Head, v, 0) | this fires "v" which is your value (orb).
   This makes the game think you touched the orb with your head causing you to collect it.
      
3. after the v you see a 1 and a 0. This basically means 0 is touching and 1 is you let go.
      
If you still didnt understand then Dynamic has some great tutorials about this on his YT.\n
""")

time.sleep(1)
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{BLUE}Now you wil learn how to do magnitude checks!{RESET}")

print("Magnitude checks basically check distance and are usually used for sliders!")

print(f"""
Lets take our print football script from earilier and modify it.
      
      for i, v in pairs(game.workspace:GetChildren()) do
        if v.Name == "Football" and v:IsA("BasePart") then
            local distance = (game.Players.LocalPlayer.Character.Torso.Position - v.Position).magnitude
            print("The ball is "..distance.." studs away!")
        end
    end
      
In the code above we added a distance variable. Lets explain how this works
      
1. We subtract the position of our torso by the position of the ball.
2. We close that equation in parenthesis and add .magnitude
3. We added a print that shows the distance in the F9 console
""")

time.sleep(1)
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{BLUE}Ok now ima teach your bitchass loops.{RESET}")

print("""
Loops can be made in multiple ways. Here is a few examples
      
while true do
    task.wait()
    print("Loop!")
end
      
while variable do
    task.wait()
    print("This is a loop")
end
      
Ok those are some basic loops and im not gonna go into too much depth on them. Just remember to add a wait so you dont crash.
""")

time.sleep(1)
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{BLUE}Pcalls.{RESET}")

print(f"""
pcalls are good to prevent something from erroring if it doesnt exist yet. Example below
      
      while true do
        task.wait()
      
        pcall(function()
            print(game.Players.LocalPlayer.Character.HumanoidRootPart) {GREEN} -- Prevents from erroring if you died and it doesnt exist{RESET}
      end)
   end
""")

time.sleep(1)
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

print(f"{BLUE}Ok now ima show your ass how to add your code into a gui.{RESET}")
input(f"{BLUE}Press enter to continue | WARNING lots of code you might have to scroll up{RESET}")

os.system('cls' if os.name == 'nt' else 'clear')

print("For this explanation i will use Orion UI which can be found here -- https://github.com/shlexware/Orion/blob/main/Documentation.md")

print(f'''
Ima be showing an example of a simple simulator autofarm.
      
      local OrionLib = loadstring(game:HttpGet(('https://raw.githubusercontent.com/shlexware/Orion/main/source')))() {GREEN}-- Initialize UI{RESET}

      local Window = OrionLib:MakeWindow({{Name = "vFishy Teaches fucking lua", HidePremium = false, SaveConfig = true, ConfigFolder = "OrionTest"}}) {GREEN}-- make a window{RESET}

      local Tab = Window:MakeTab({{ {GREEN}-- Makes a tab called "Main"{RESET}
        Name = "Main",
        PremiumOnly = false
      }})

      local af = false {GREEN} -- Making variable to store value{RESET}

      Tab:AddToggle({{ {GREEN} -- Makes a toggle{RESET}
        Name = "AutoFarm",
        Default = false,
        Callback = function(v)
            af = v {GREEN} --makes the af variable equal toggle value {RESET}
        end    
    }})

    task.spawn(function() {GREEN} -- I personally make my loops in spawn functions since slixx taught me this way{RESET}
        while true do
            task.wait()

            if not af then {GREEN} -- turns off the code if toggle is false{RESET}
                continue
            end

            if af then {GREEN} -- Check if toggle is on{RESET}
                game:GetService("ReplicatedStorage").Remotes.AddSpeed:FireServer() {GREEN} -- Fires remote to give our player speed{RESET}
            end
        end
    end)

    OrionLib:Init()\n\n
''')
time.sleep(3)
print(f"{BLUE}Great! You learned how to make shit toggleable within an UI.{RESET}")
input(f"{BLUE}Press enter to continue{RESET}")
os.system('cls' if os.name == 'nt' else 'clear')

input(f"{BLUE}Tell vFishy thanks for the beautiful ass tutorial he wasted 2 hours making. Thanks for learning lua here and not my dms!{RESET}")
input("")
input("")
