import customtkinter as ctk


class OperationSettingsPage:
    """Operation Settings page with three mode sections"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_operation_settings_page()
    
    def create_operation_settings_page(self):
        """Create the Operation Settings page layout"""
        # Main container
        main_container = ctk.CTkFrame(self.parent_frame, fg_color="#F5F5F5")
        main_container.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Operation Mode Section
        self.create_operation_mode_section(main_container)
        
        # Drive Mode Section
        self.create_drive_mode_section(main_container)
        
        # Regeneration Mode Section
        self.create_regeneration_mode_section(main_container)
    
    def create_operation_mode_section(self, parent):
        """Create Operation Mode section"""
        # Section container
        section = ctk.CTkFrame(parent, fg_color="transparent")
        section.pack(fill="x", pady=(0, 30))
        
        # Header with gradient effect (yellow to orange)
        header = ctk.CTkLabel(
            section,
            text="Operation Mode",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2D2D2D",
            fg_color="#FFB84D",  # Orange color
            corner_radius=20,
            height=45,
            width=200
        )
        header.pack(anchor="w", pady=(0, 10))
        
        # Gray container for buttons
        button_container = ctk.CTkFrame(section, fg_color="#D9D9D9", corner_radius=20)
        button_container.pack(fill="x", pady=(0, 0))
        
        # Button frame
        button_frame = ctk.CTkFrame(button_container, fg_color="transparent")
        button_frame.pack(padx=30, pady=30)
        
        # Torque Mode button
        torque_btn = ctk.CTkButton(
            button_frame,
            text="Torque Mode",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white",
            fg_color="#4D9EFF",
            hover_color="#3D8EEF",
            corner_radius=25,
            width=160,
            height=50
        )
        torque_btn.pack(side="left", padx=(0, 20))
        
        # Speed Mode button
        speed_btn = ctk.CTkButton(
            button_frame,
            text="Speed Mode",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white",
            fg_color="#4D9EFF",
            hover_color="#3D8EEF",
            corner_radius=25,
            width=160,
            height=50
        )
        speed_btn.pack(side="left")
    
    def create_drive_mode_section(self, parent):
        """Create Drive Mode section"""
        # Section container
        section = ctk.CTkFrame(parent, fg_color="transparent")
        section.pack(fill="x", pady=(0, 30))
        
        # Header with gradient effect (yellow to orange)
        header = ctk.CTkLabel(
            section,
            text="Drive Mode",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2D2D2D",
            fg_color="#FFB84D",  # Orange color
            corner_radius=20,
            height=45,
            width=200
        )
        header.pack(anchor="w", pady=(0, 10))
        
        # Gray container for buttons
        button_container = ctk.CTkFrame(section, fg_color="#D9D9D9", corner_radius=20)
        button_container.pack(fill="x", pady=(0, 0))
        
        # Button frame
        button_frame = ctk.CTkFrame(button_container, fg_color="transparent")
        button_frame.pack(padx=30, pady=30)
        
        # Drive by can button
        drive_can_btn = ctk.CTkButton(
            button_frame,
            text="Drive by can",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white",
            fg_color="#4D9EFF",
            hover_color="#3D8EEF",
            corner_radius=25,
            width=160,
            height=50
        )
        drive_can_btn.pack(side="left", padx=(0, 20))
        
        # Analog Input Control button
        analog_btn = ctk.CTkButton(
            button_frame,
            text="Analog Input\nControl",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white",
            fg_color="#4D9EFF",
            hover_color="#3D8EEF",
            corner_radius=25,
            width=160,
            height=50
        )
        analog_btn.pack(side="left")
    
    def create_regeneration_mode_section(self, parent):
        """Create Regeneration Mode section"""
        # Section container
        section = ctk.CTkFrame(parent, fg_color="transparent")
        section.pack(fill="x", pady=(0, 0))
        
        # Header with gradient effect (yellow to orange)
        header = ctk.CTkLabel(
            section,
            text="Regeneration Mode",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#2D2D2D",
            fg_color="#FFB84D",  # Orange color
            corner_radius=20,
            height=45,
            width=220
        )
        header.pack(anchor="w", pady=(0, 10))
        
        # Gray container for button
        button_container = ctk.CTkFrame(section, fg_color="#D9D9D9", corner_radius=20)
        button_container.pack(fill="x", pady=(0, 0))
        
        # Button frame
        button_frame = ctk.CTkFrame(button_container, fg_color="transparent")
        button_frame.pack(padx=30, pady=30)
        
        # Enabled/Disabled button
        regen_btn = ctk.CTkButton(
            button_frame,
            text="Enabled/\nDisabled",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white",
            fg_color="#4D9EFF",
            hover_color="#3D8EEF",
            corner_radius=25,
            width=160,
            height=50
        )
        regen_btn.pack(side="left")
