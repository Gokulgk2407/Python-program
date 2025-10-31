import customtkinter as ctk


class SystemControlParametersPage:
    """System Control Parameters page with 5 tabs containing tables"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_system_control_parameters_page()
    
    def create_system_control_parameters_page(self):
        """Create the System Control Parameters page with tabs"""
        # Main container
        main_container = ctk.CTkFrame(self.parent_frame, fg_color="#F5F5F5")
        main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Tab header container
        tab_header = ctk.CTkFrame(main_container, fg_color="#D9D9D9", height=60)
        tab_header.pack(fill="x", padx=0, pady=0)
        tab_header.pack_propagate(False)
        
        # Tab buttons frame
        tab_buttons_frame = ctk.CTkFrame(tab_header, fg_color="transparent")
        tab_buttons_frame.pack(pady=10, padx=20)
        
        # Tab names
        tabs = [
            "Speed PI\nTuning",
            "Thermal\nTuning",
            "Phase Current\noffset/Gain",
            "Encoder\nOffset",
            "Speed\nLimit"
        ]
        
        self.active_tab = "Speed PI\nTuning"
        self.tab_buttons = {}
        
        # Create tab buttons
        for tab_name in tabs:
            btn = ctk.CTkButton(
                tab_buttons_frame,
                text=tab_name,
                font=ctk.CTkFont(size=12),
                text_color="#666666",
                fg_color="transparent",
                hover_color="#C9C9C9",
                width=120,
                height=45,
                corner_radius=0,
                border_width=0,
                command=lambda t=tab_name: self.switch_tab(t)
            )
            btn.pack(side="left", padx=2)
            self.tab_buttons[tab_name] = btn
        
        # Content area
        self.content_area = ctk.CTkFrame(main_container, fg_color="#F5F5F5")
        self.content_area.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Load initial tab
        self.switch_tab("Speed PI\nTuning")
    
    def switch_tab(self, tab_name):
        """Switch between tabs"""
        self.active_tab = tab_name
        
        # Update tab button styles - add pink underline to active
        for name, btn in self.tab_buttons.items():
            if name == tab_name:
                btn.configure(fg_color="#E9E9E9", border_width=0, border_color="#FF1493")
            else:
                btn.configure(fg_color="transparent", border_width=0)
        
        # Clear content
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        # Load tab content
        if tab_name == "Speed PI\nTuning":
            self.create_speed_pi_tuning_tab()
        elif tab_name == "Thermal\nTuning":
            self.create_thermal_tuning_tab()
        elif tab_name == "Phase Current\noffset/Gain":
            self.create_phase_current_tab()
        elif tab_name == "Encoder\nOffset":
            self.create_encoder_offset_tab()
        elif tab_name == "Speed\nLimit":
            self.create_speed_limit_tab()
    
    def create_table(self, parent, rows_data, width=350):
        """Helper to create a table with 2 columns"""
        table = ctk.CTkFrame(parent, fg_color="white", border_width=1, border_color="#333333")
        table.pack(pady=10, anchor="w")
        
        # Configure columns
        table.grid_columnconfigure(0, minsize=width//2)
        table.grid_columnconfigure(1, minsize=width//2)
        
        for idx, (label, is_highlighted) in enumerate(rows_data):
            # Determine background color
            bg_color = "#C8E6C9" if is_highlighted else "#FFFFFF"
            
            # Left cell (label)
            left_cell = ctk.CTkFrame(table, fg_color=bg_color, border_width=1, border_color="#333333")
            left_cell.grid(row=idx, column=0, sticky="nsew")
            
            left_label = ctk.CTkLabel(
                left_cell,
                text=label,
                font=ctk.CTkFont(size=12),
                text_color="#000000",
                anchor="w"
            )
            left_label.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Right cell (empty)
            right_cell = ctk.CTkFrame(table, fg_color=bg_color, border_width=1, border_color="#333333")
            right_cell.grid(row=idx, column=1, sticky="nsew")
            
            right_label = ctk.CTkLabel(right_cell, text="", text_color="#000000")
            right_label.pack(fill="both", expand=True, padx=10, pady=10)
        
        return table
    
    def create_speed_pi_tuning_tab(self):
        """Create Speed PI Tuning tab content"""
        rows = [
            ("Enable Tuning", False),
            ("Kp", True),
            ("KI", False)
        ]
        self.create_table(self.content_area, rows)
    
    def create_thermal_tuning_tab(self):
        """Create Thermal Tuning tab content"""
        # First table
        rows1 = [
            ("Enable Tuning", False),
            ("Motor Temperature Limit 1", True),
            ("Controller temperature Limit 1", False),
            ("Inverter temperature Limit 1", False)
        ]
        self.create_table(self.content_area, rows1, width=400)
        
        # Spacing
        ctk.CTkFrame(self.content_area, fg_color="transparent", height=20).pack()
        
        # Second table
        rows2 = [
            ("Reset to Default Value", False),
            ("PresetMotor Temperature Limit 1", True),
            ("Preset Controller temperature Limit 1", False),
            ("Preset Inverter temperature Limit 1", False)
        ]
        self.create_table(self.content_area, rows2, width=400)
    
    def create_phase_current_tab(self):
        """Create Phase Current offset/Gain tab content"""
        # Container for all tables
        container = ctk.CTkFrame(self.content_area, fg_color="transparent")
        container.pack(fill="both", expand=True)
        
        # Left side
        left_frame = ctk.CTkFrame(container, fg_color="transparent")
        left_frame.pack(side="left", anchor="nw", padx=(0, 20))
        
        rows_left = [
            ("Enable Calibration", False),
            ("Phase A Offset", True),
            ("Phase B Offset", False),
            ("Phase C Offset", True),
            ("Phase A Gain", False),
            ("Phase B Gain", True),
            ("Phase C Gain", False)
        ]
        self.create_table(left_frame, rows_left, width=350)
        
        # Right side
        right_frame = ctk.CTkFrame(container, fg_color="transparent")
        right_frame.pack(side="left", anchor="nw")
        
        # Top right table
        rows_top_right = [("Electrical Angle Offset", False)]
        self.create_table(right_frame, rows_top_right, width=400)
        
        # Spacing
        ctk.CTkFrame(right_frame, fg_color="transparent", height=20).pack()
        
        # Bottom right table
        rows_bottom_right = [
            ("Reset To Default Value", False),
            ("Factory Phase A Offset", True),
            ("Factory Phase B Offset", False),
            ("Factory Phase C Offset", True),
            ("Factory Phase A Gain", False),
            ("Factory Phase B Gain", True),
            ("Factory Phase C Offset", False)
        ]
        self.create_table(right_frame, rows_bottom_right, width=400)
    
    def create_encoder_offset_tab(self):
        """Create Encoder Offset tab content (empty)"""
        # Empty content
        pass
    
    def create_speed_limit_tab(self):
        """Create Speed Limit tab content"""
        rows = [("Maximum Speed Limit", False)]
        self.create_table(self.content_area, rows, width=400)
