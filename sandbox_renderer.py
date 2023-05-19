import customtkinter
import os
from PIL import Image
from overlay import Overlay
from capture import Capture
import numpy as np

#button color : 3a7ebf

class App(customtkinter.CTk):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Lorem.png")), size=(500, 300))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Lorem.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "main_icon.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "main_icon.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Lorem.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "Lorem.png")), size=(20, 20))
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

        


        def label_button_frame_event(self, item):
            print(f"label button frame clicked: {item}")

        # create overlay window
        self.toplevel_window = None

        # select default frame
        self.select_frame_by_name("home")

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

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")

    def home_frame_start_button_clicked(self):
        if self.toplevel_window is None:
            self.toplevel_window = Overlay(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.win.destroy()
            self.toplevel_window = Overlay(self)  # if window exists focus it

    def home_frame_detect_button_clicked(self):
        print(f"label button frame clicked")
        combobox_value=[]
        Capture.list_window_names(combobox_value)
        self.home_frame_combobox.configure(values=combobox_value)
        self.home_frame_combobox.set(combobox_value[0])
########
########

def while_loop(selected_str):
    file_name = ""


########
########
if __name__ == "__main__":
    app = App()
    app.mainloop()