import sys 
import subprocess
from tkinter import *
from src.function.function import function_Encontrar_A_Sala
import os

try: 
    import ttkbootstrap as ttk
    from ttkbootstrap.constants import *
    from ttkbootstrap.style import Style
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ttkbootstrap'])
finally:
    import ttkbootstrap as ttk
    from ttkbootstrap.constants import *
    from ttkbootstrap.style import Style

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

def handle_principal_aba():
    try:
        numero_participantes = int(numero_participantes_Entry.get())
        numero_participantes_Entry.delete(0, END)
        
        # Chama a função e obtém o resultado
        resultado = function_Encontrar_A_Sala(numero_participantes)
        
        # Atualiza o label de resultados
        resultados_Label.config(text=resultado)
    
    except ValueError:
        resultados_Label.config(text='Digite apenas números')

janela = ttk.Window()
janela.title("Sala Ideal")
janela.geometry("1000x780+550+125")
janela.resizable(True, True)
janela.iconbitmap(r'src\icon\meetings_meeting_table_people_work_icon_144587.ico')
style = Style(theme="flatly")

main_frame = ttk.Frame(janela)
main_frame.pack(padx=10, pady=10, fill='both', expand=False)
ttk.Label(main_frame, text="Qual A Sala Ideal Para Uma Reuniao", font=('', 18)).pack(padx=10, pady=10, fill='y')

numero_participantes = ttk.Frame(main_frame)
numero_participantes.pack(padx=5, pady=5, fill='x')
numero_participantes_Label = ttk.Label(numero_participantes, text="Coloque o numero de Participantes:", font=('', 15))
numero_participantes_Label.pack(side=LEFT, padx=5, pady=5, fill='x')

numero_participantes_Entry = ttk.Entry(numero_participantes, font=("arial", 12))
numero_participantes_Entry.pack(padx=5, side=LEFT, fill="x", expand=True)

Rodar_button = ttk.Button(main_frame, text="Encontrar", command=handle_principal_aba, bootstyle=OUTLINE)
Rodar_button.pack(expand=True, fill='both')

resultados_janela = ttk.Frame(main_frame)
resultados_janela.pack(padx=10, fill='x')
resultados_Label = ttk.Label(resultados_janela, text="", font=("arial", 15))
resultados_Label.pack(padx=10, pady=10, fill='x', expand=True)

janela.mainloop()
