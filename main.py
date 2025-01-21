import customtkinter
import os
from PIL import Image
from overlay import Overlay
from capture import Capture
from savecsv import SaveCsv
from asyncio.windows_events import NULL
from ocr import Tesseract_Ocr
from translate import TranslatorPapago

class App(customtkinter.CTk):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    window_name = None
    toplevel_window = None

    def __init__(self):
        super().__init__()

        self.title("Bridge - RealtimeOverlayTranslator")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "main_icon.png")), size=(32, 32))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "img1.png")), size=(500, 300))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Lorem.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "main_icon.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "main_icon.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "main_icon.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "main_icon.png")), size=(20, 20))
        self.setting_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "setting_icon.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "setting_icon.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Bridge", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Detect Window",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Setting",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.setting_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0,column=0, padx=20, pady=10)

        self.home_frame_detect_button = customtkinter.CTkButton(self.home_frame, width=500, text="Detect Window", command=self.home_frame_detect_button_clicked)
        self.home_frame_detect_button.grid(row=1, column=0, padx=20, pady=5)

        self.home_frame_start_button = customtkinter.CTkButton(self.home_frame, width=500, text="Start", compound="bottom", state="disabled", command=self.home_frame_start_button_clicked)
        self.home_frame_start_button.grid(row=3, column=0, padx=20, pady=5)

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
            if(self.home_frame_start_button.cget("state") == "disabled"):
                self.home_frame_start_button.configure(state="normal")
            self.window_name=choice

        combobox_var = customtkinter.StringVar(value="You Have to click Detect Window Button")
        self.home_frame_combobox = customtkinter.CTkComboBox(master=self.home_frame,
                                            width=500,
                                            values=[], # set initial value
                                            command=combobox_callback,
                                            variable=combobox_var)
        self.home_frame_combobox.grid(row=2, column=0, padx=20, pady=5)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.setup_settings_frame()

        # select default frame
        self.select_frame_by_name("home")

    def setup_settings_frame(self):
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.label_client_id = customtkinter.CTkLabel(self.third_frame, text="Client ID:")
        self.label_client_id.grid(row=0, column=0, padx=20, pady=10)
        self.entry_client_id = customtkinter.CTkEntry(self.third_frame)
        self.entry_client_id.grid(row=1, column=0, padx=20, pady=10)
        self.entry_client_id.insert(0, TranslatorPapago().client_id)

        self.label_client_secret = customtkinter.CTkLabel(self.third_frame, text="Client Secret:")
        self.label_client_secret.grid(row=2, column=0, padx=20, pady=10)
        self.entry_client_secret = customtkinter.CTkEntry(self.third_frame)
        self.entry_client_secret.grid(row=3, column=0, padx=20, pady=10)
        self.entry_client_secret.insert(0, TranslatorPapago().client_secret)

        self.save_button = customtkinter.CTkButton(self.third_frame, text="Save", command=self.save_settings)
        self.save_button.grid(row=4, column=0, padx=20, pady=20)

    def save_settings(self):
        new_client_id = self.entry_client_id.get()
        new_client_secret = self.entry_client_secret.get()
        TranslatorPapago().set_client_id(new_client_id)
        TranslatorPapago().set_client_secret(new_client_secret)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def home_frame_start_button_clicked(self):
        if self.toplevel_window is None:
            self.toplevel_window = Overlay()  # create window if its None or destroyed
            self.toplevel_window.win.after(1000,while_loop,self.window_name)
            self.toplevel_window.win.mainloop()
        else:
            self.toplevel_window.win.destroy()
            self.toplevel_window = Overlay()  # if window exists focus it
            self.toplevel_window.win.after(1000,while_loop,self.window_name)
            self.toplevel_window.win.mainloop()

    def home_frame_detect_button_clicked(self):
        print(f"label button frame clicked")
        combobox_value=[]
        Capture.list_window_names(combobox_value)
        self.home_frame_combobox.configure(values=combobox_value)
        self.home_frame_combobox.set(combobox_value[0])

def on_closing():
    if not app.toplevel_window is None:
        app.toplevel_window.win.destroy()
    app.destroy()

def while_loop(selected_window_name):
    print("Call While loop-list declare")

    S_dict = list()
    detected_word_array = []
    be_verb = ['am','be','are','is','was','were','was','i','you','we','he','she','it','we','they','will', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', 'your', 'my', 'me', 'mine', 'yours'] # Be 동사는 단어장에 안들어감

    if not selected_window_name is None:
        print("Call While loop-checking window name")
        Caps=Capture(selected_window_name)
        Scsv=SaveCsv(selected_window_name)
        Trans=TranslatorPapago()
        Ocrs=Tesseract_Ocr()

    else:
        print("Call While loop-checking window name-fail")
        return

    print("Call While loop-start process")
    S_dict.clear()
    arr=Caps.get_rect()
    screenshot = Caps.get_screenshot()
    minimum_left=10000
    minimum_top=10000
    result,str_result = Ocrs.get_ocr_tesseract(screenshot)

    for i in range(0, len(result["text"])):
        text = result["text"][i]
        conf = int(result["conf"][i])
        print("Call While loop-first for")
        if(((result["left"][i-1]+result["width"][i-1]+result["height"][i-1]<result["left"][i])
            or result["top"][i-1]+result["height"][i-1]*1.2 < result["top"][i]) or i == len(result["text"])):
            final_result = " ".join(detected_word_array)
            detected_word_array.clear()
            if(final_result == NULL or len(final_result) <= 1 or  final_result.isspace() == True):
                continue
            print("Call While loop-2 if")

            search_text = Scsv.search(final_result)
            if(search_text == False):
                temp_text = final_result
                if(len(temp_text) > 1):
                    print(final_result)
                    final_result = Trans.get_translate(final_result, 'en', 'ko')
                    Scsv.save_dictionary(temp_text,final_result)
                temp_text = NULL
            else:
                final_result = search_text
            print("Call While loop-3 if")
            search_text = NULL
            if(len(final_result) >= 1):
                app.toplevel_window.labeler(final_result, minimum_left+arr[0], minimum_top+arr[1],
                    result["left"][i]-minimum_left+result["width"][i], result["top"][i]-minimum_top+result["height"][i], 11)
            minimum_left=10000
            minimum_top=10000
        elif(conf>70):#need to add
            tmptext = "".join([c if ord(c)<128 else "" for c in text]).strip()
            S_dict.append(tmptext)
            minimum_left = result["left"][i] if minimum_left > result["left"][i] else minimum_left
            minimum_top = result["top"][i] if minimum_top > result["top"][i] else minimum_top
            detected_word_array.append(tmptext)
    print("Call While loop-update")
    app.toplevel_window.win.update()
    app.toplevel_window.win.after(1000,while_loop, app.window_name)

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()