import customtkinter as ctk


class FirmwarePage:
    """Firmware page with tabbed interface for Motor Controller Info and Bootloader Info"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_firmware_page()
    
    def create_firmware_page(self):
        """Create the Firmware page layout with tabs positioned ON violet stripe"""
        # Main container
        main_container = ctk.CTkFrame(self.parent_frame, fg_color="#F5F5F5")
        main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Violet diagonal stripe
        violet_stripe = ctk.CTkFrame(main_container, fg_color="#B8B3D4", height=70, corner_radius=0)
        violet_stripe.pack(fill="x", pady=(0, 0))
        violet_stripe.pack_propagate(False)
        
        # Tab buttons positioned ON the violet stripe
        tab_button_frame = ctk.CTkFrame(violet_stripe, fg_color="transparent")
        tab_button_frame.pack(side="bottom", anchor="w", padx=20, pady=5)
        
        self.active_tab = "Motor Controller Info"
        
        # Motor Controller Info tab button
        self.motor_controller_btn = ctk.CTkButton(
            tab_button_frame,
            text="Motor Controller Info",
            fg_color="#A8E6A1",
            hover_color="#95D88F",
            text_color="#2D2D2D",
            corner_radius=8,
            height=35,
            font=ctk.CTkFont(size=13),
            command=lambda: self.switch_tab("Motor Controller Info")
        )
        self.motor_controller_btn.pack(side="left", padx=(0, 5))
        
        # Bootloader Info tab button
        self.bootloader_btn = ctk.CTkButton(
            tab_button_frame,
            text="Bootloader Info",
            fg_color="#B8B3D4",
            hover_color="#C8C3E4",
            text_color="#2D2D2D",
            corner_radius=8,
            height=35,
            font=ctk.CTkFont(size=13),
            command=lambda: self.switch_tab("Bootloader Info")
        )
        self.bootloader_btn.pack(side="left", padx=(0, 5))
        
        # Content area
        self.content_frame = ctk.CTkFrame(main_container, fg_color="#E8E8E8")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Show initial tab content
        self.switch_tab("Motor Controller Info")
    
    def switch_tab(self, tab_name):
        """Switch between tabs and update content"""
        self.active_tab = tab_name
        
        # Update button colors
        if tab_name == "Motor Controller Info":
            self.motor_controller_btn.configure(fg_color="#A8E6A1")
            self.bootloader_btn.configure(fg_color="#B8B3D4")
        else:
            self.motor_controller_btn.configure(fg_color="#B8B3D4")
            self.bootloader_btn.configure(fg_color="#A8E6A1")
        
        # Clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Load new content
        if tab_name == "Motor Controller Info":
            self.create_motor_controller_info(self.content_frame)
        elif tab_name == "Bootloader Info":
            self.create_bootloader_info(self.content_frame)
    
    def create_motor_controller_info(self, parent):
        """Create exact table with fixed columns and extending rows"""
        # Table container with fixed width, centered
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(expand=True, fill="y", padx=50, pady=20)
        
        # Table with fixed width, border
        table = ctk.CTkFrame(container, fg_color="white", width=430, border_width=2, border_color="#333333")
        table.pack(expand=True, fill="y")
        table.pack_propagate(False)
        
        # Header
        header = ctk.CTkLabel(
            table,
            text="Motor Controller Info",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#000000",
            fg_color="#A8E6A1",
            corner_radius=0,
            height=45
        )
        header.pack(fill="x")
        
        # Create table frame for rows
        rows_frame = ctk.CTkFrame(table, fg_color="white")
        rows_frame.pack(fill="both", expand=True)
        
        # Configure grid to expand rows vertically
        rows_frame.grid_columnconfigure(0, minsize=215)
        rows_frame.grid_columnconfigure(1, minsize=215)
        
        # Fields
        fields = [
            "Model Name",
            "Inverter Version", 
            "Controller Version",
            "Encoder Version",
            "Firmware",
            "Housing Version",
            "",  # Empty row
            ""   # Empty row
        ]
        
        # Equal weight for all rows to fill space
        for i in range(len(fields)):
            rows_frame.grid_rowconfigure(i, weight=1, uniform="row")
        
        # Create rows
        for idx, field in enumerate(fields):
            # Left cell (title)
            left_cell = ctk.CTkFrame(
                rows_frame, 
                fg_color="white",
                border_width=1,
                border_color="#333333"
            )
            left_cell.grid(row=idx, column=0, sticky="nsew")
            
            left_label = ctk.CTkLabel(
                left_cell,
                text=field,
                font=ctk.CTkFont(size=13),
                text_color="#000000",
                anchor="w"
            )
            left_label.pack(fill="both", expand=True, padx=15, pady=10)
            
            # Right cell (empty)
            right_cell = ctk.CTkFrame(
                rows_frame,
                fg_color="white",
                border_width=1,
                border_color="#333333"
            )
            right_cell.grid(row=idx, column=1, sticky="nsew")
            
            right_label = ctk.CTkLabel(
                right_cell,
                text="",
                font=ctk.CTkFont(size=13),
                text_color="#000000"
            )
            right_label.pack(fill="both", expand=True, padx=15, pady=10)
    
    def create_bootloader_info(self, parent):
        """Create exact table with fixed columns and extending rows"""
        # Table container with fixed width, centered
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(expand=True, fill="y", padx=50, pady=20)
        
        # Table with fixed width, border
        table = ctk.CTkFrame(container, fg_color="white", width=430, border_width=2, border_color="#333333")
        table.pack(expand=True, fill="y")
        table.pack_propagate(False)
        
        # Header
        header = ctk.CTkLabel(
            table,
            text="Bootloader Info",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#000000",
            fg_color="#A8E6A1",
            corner_radius=0,
            height=45
        )
        header.pack(fill="x")
        
        # Create table frame for rows
        rows_frame = ctk.CTkFrame(table, fg_color="white")
        rows_frame.pack(fill="both", expand=True)
        
        # Configure grid to expand rows vertically
        rows_frame.grid_columnconfigure(0, minsize=215)
        rows_frame.grid_columnconfigure(1, minsize=215)
        
        # Fields - Model Name + empty rows
        fields = ["Model Name"] + [""] * 7  # Model Name + 7 empty rows
        
        # Equal weight for all rows to fill space
        for i in range(len(fields)):
            rows_frame.grid_rowconfigure(i, weight=1, uniform="row")
        
        # Create rows
        for idx, field in enumerate(fields):
            # Left cell (title)
            left_cell = ctk.CTkFrame(
                rows_frame, 
                fg_color="white",
                border_width=1,
                border_color="#333333"
            )
            left_cell.grid(row=idx, column=0, sticky="nsew")
            
            left_label = ctk.CTkLabel(
                left_cell,
                text=field,
                font=ctk.CTkFont(size=13),
                text_color="#000000",
                anchor="w"
            )
            left_label.pack(fill="both", expand=True, padx=15, pady=10)
            
            # Right cell (empty)
            right_cell = ctk.CTkFrame(
                rows_frame,
                fg_color="white",
                border_width=1,
                border_color="#333333"
            )
            right_cell.grid(row=idx, column=1, sticky="nsew")
            
            right_label = ctk.CTkLabel(
                right_cell,
                text="",
                font=ctk.CTkFont(size=13),
                text_color="#000000"
            )
            right_label.pack(fill="both", expand=True, padx=15, pady=10)
