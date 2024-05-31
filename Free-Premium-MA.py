import requests
from colorama import Fore
from rich.console import Console
from rich.table import Table
from rich import box
from rich import align
try:
    console = Console()
    print(f"""{Fore.RED} 
    ██████╗  █████╗ ██████╗ ██╗  ██╗ 
    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝ 
    ██║  ██║███████║██████╔╝█████╔╝  
    ██║  ██║██╔══██║██╔══██╗██╔═██╗  
    ██████╔╝██║  ██║██║  ██║██║  ██╗ 
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ 
                                    
    ██████╗ ██╗     ██╗   ██╗██████╗ 
    ██╔══██╗██║     ██║   ██║██╔══██╗
    ██████╔╝██║     ██║   ██║██║  ██║
    ██╔══██╗██║     ██║   ██║██║  ██║
    ██████╔╝███████╗╚██████╔╝██████╔╝
    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ 
                                    
    """)

    def print_Data(Name , Des , Author):
        # table = Name | Des | Author
        console.log(log_locals=True )
    print_Data({"Name" : "MA Premium"},{"Des":"A tool to use free premium of MovieJavan and AnimeOn"},{"Author":"DarkBlud"})

    def command():
        global console
        table = Table(title="Commands" ,box=box.ROUNDED)

        table.add_column("Num", style="cyan" , vertical="middle")
        table.add_column("Command" ,style="green" , vertical="middle")

        # table.add_row("1 ","Get directories of MovieJavan\n")
        # table.add_row("2 ","Get directories of AnimeOn \n")
        table.add_row("1 ","Search MovieJavan for a Movie\n")
        table.add_row("2 ","Search AnimeOn for an Anime ")

        console.print(table)

    command()



    dlnum = 0 



    def SM():
        
        try:
            movie_name = input(f"{Fore.CYAN}  Please enter the movie name({Fore.RED} It must be specific {Fore.CYAN})\n {Fore.LIGHTBLUE_EX} Example : Three.muskeeters ( use . instead of space )  \n: ")
            if movie_name not in ["",None," "] :
                print(f"{Fore.YELLOW} Searching for movie in list (It might take some minutes do to the big database) \n ")
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36"
                }
                a = 1 
                table = Table(title="Founded links" , box=box.ROUNDED)

                table.add_column("Num" , style="white")
                table.add_column("Links" , style="green")
                with open("database/hits.txt", "r") as file:
                    for line in file:
                        url = line.strip() + f"?filter={movie_name}"
                        response = requests.get(url=url, headers=headers)

                        # Check if the response status code is 200 (OK)
                        if response.status_code == 200:
                            # Check if the movie name appears in any of the list items
                            if movie_name.lower() in response.text.lower():
                                
                                table.add_row(f"{a}",f"{url}")
                                
                                a += 1 
                            
                    console.print(table)
                        # else:
                        #     print(f"{Fore.RED}Error accessing {url}: Status Code {response.status_code}")
            else : 
                print(f"{Fore.RED} \n You must enter a movie name !")
        except KeyboardInterrupt:
            print(f"{Fore.RED} \nEnding program...")
            exit()
        except KeyError as e:
            print(f"{Fore.RED} \nAn error has occurred: {e}")
            exit()


    def SA():
        

        try:
            movie_name = input(f"{Fore.CYAN}  Please enter the anime name({Fore.RED} It must be specific {Fore.CYAN})\n {Fore.LIGHTBLUE_EX} Example : Three.muskeeters ( use . instead of space )  \n: ")
            if movie_name not in ["",None," "] :
                print(f"{Fore.YELLOW} Searching for anime in list (It might take some minutes do to the big database) \n ")
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36"
                }
                a = 1 
                table = Table(title="Founded links" , box=box.ROUNDED)

                table.add_column("Num" , style="white")
                table.add_column("Links" , style="green")
                with open("database/hits-anime.txt", "r") as file:
                    for line in file:
                        url = line.strip() + f"?filter={movie_name}"
                        response = requests.get(url=url, headers=headers)

                        # Check if the response status code is 200 (OK)
                        if response.status_code == 200:
                            # Check if the movie name appears in any of the list items
                            if movie_name.lower() in response.text.lower():
                                
                                table.add_row(f"{a}",f"{url}")
                                
                                a += 1 
                            
                    console.print(table)
                        # else:
                        #     print(f"{Fore.RED}Error accessing {url}: Status Code {response.status_code}")
            else : 
                print(f"{Fore.RED} \n You must enter a anime name !")
        except KeyboardInterrupt:
            print(f"{Fore.RED} \nEnding program...")
            exit()
        except KeyError as e:
            print(f"{Fore.RED} \nAn error has occurred: {e}")
            exit()

    try : 
        choice = int(input(f"{Fore.WHITE} : "))
    except ValueError : 
        print(f"{Fore.RED}\nYou must Enter a number not text...")
        exit()
    if 0<choice<5 :
        if choice == 1 : 
            SM()
        elif choice == 2 :
            SA()
        # elif choice == 3 :
        #     SM() 
        # elif choice == 4 : 
        else:
            print(f"{Fore.RED} \nWrong choice ")
            exit()
    else:
        print(f"{Fore.RED} You must select a option 1-4")
        exit()
except KeyboardInterrupt:
    print(f"{Fore.RED} \nEnding program...")
    exit()
except KeyError as e:
    print(f"{Fore.RED} \nAn error has occurred: {e}")
    exit()

        