import customtkinter as ctk


class SystemStatusPage:
    """System Status page with multiple tabs and data displays"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_system_status_page()
    
    def create_system_status_page(self):
        """Create the System Status page layout with tabs"""
        # Main container
        main_container = ctk.CTkFrame(self.parent_frame, fg_color="white", corner_radius=10)
        main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Create tabview
        self.tabview = ctk.CTkTabview(
            main_container,
            segmented_button_selected_color="#C77DFF",
            segmented_button_selected_hover_color="#B86BEE",
        )
        self.tabview.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Add tabs
        tab_names = [
            "Drive Monitoring\nSignals",
            "Current & Voltage\nSignals",
            "Control\nInputs",
            "Speed Loop\nPI Gains",
            "Thermal\nStatus",
            "Can Communication\nStatus",
        ]
        
        self.tabs = {}
        for name in tab_names:
            self.tabs[name] = self.tabview.add(name)
        
        # Populate each tab
        self.create_drive_monitoring_tab()
        self.create_current_voltage_tab()
        self.create_control_inputs_tab()
        self.create_speed_loop_tab()
        self.create_thermal_status_tab()
        self.create_can_communication_tab()
    
    def create_drive_monitoring_tab(self):
        """Create Drive Monitoring Signals tab content"""
        tab = self.tabs["Drive Monitoring\nSignals"]
        
        # Table container
        table_container = ctk.CTkFrame(tab, fg_color="#F7F7F7")
        table_container.pack(padx=20, pady=20, anchor="w")
        
        # Create table
        table_frame = ctk.CTkFrame(table_container, fg_color="white", corner_radius=0)
        table_frame.pack()
        
        # Define rows
        rows = [
            "Actual Speed(RPM)",
            "Reference Speed(RPM)",
            "Reference Torque(Nm)",
            "Max Speed Limit(RPM)",
            "Encoder Count",
        ]
        
        # Create table rows
        for r, label in enumerate(rows):
            self.create_table_row(table_frame, r, label)
        
        # Column widths
        table_frame.grid_columnconfigure(0, minsize=320)
        table_frame.grid_columnconfigure(1, minsize=220)
    
    def create_current_voltage_tab(self):
        """Create Current & Voltage Signals tab content"""
        tab = self.tabs["Current & Voltage\nSignals"]
        
        # Table container
        table_container = ctk.CTkFrame(tab, fg_color="#F7F7F7")
        table_container.pack(padx=20, pady=20, anchor="w")
        
        # Create table
        table_frame = ctk.CTkFrame(table_container, fg_color="white", corner_radius=0)
        table_frame.pack()
        
        # Define rows
        rows = [
            "DC Link Voltage(V)",
            "DC Link Current(A)",
            "Phase RMS Current(A)",
            "Reference id(A)",
            "Reference Iq(A)",
            "Actual Id(A)",
            "Actual Iq(A)",
            "Reference Vd(V)",
            "Reference Vq(V)",
            "Phase Voltage(V)",
        ]
        
        # Create table rows
        for r, label in enumerate(rows):
            self.create_table_row(table_frame, r, label)
        
        # Column widths
        table_frame.grid_columnconfigure(0, minsize=320)
        table_frame.grid_columnconfigure(1, minsize=220)
    
    def create_control_inputs_tab(self):
        """Create Control Inputs tab content"""
        tab = self.tabs["Control\nInputs"]
        
        # Main container for two tables side by side
        main_frame = ctk.CTkFrame(tab, fg_color="#F7F7F7")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Left table container
        left_container = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=0)
        left_container.grid(row=0, column=0, padx=(0, 20), sticky="nw")
        
        # Left table rows
        left_rows = [
            "Throttle Input(%)",
            "Throttle ADC Count",
            "Drive State",
            "Drive Mode",
            "Regeneration Mode",
            "Motor Direction",
            "KSI Status",
            "Vehicle  Brake Status",
        ]
        
        for r, label in enumerate(left_rows):
            self.create_table_row(left_container, r, label, width1=280, width2=160)
        
        # Right table container
        right_container = ctk.CTkFrame(main_frame, fg_color="white", corner_radius=0)
        right_container.grid(row=0, column=1, sticky="nw")
        
        # Right table rows
        right_rows = [
            "Throttle Input Command",
            "Brake Command",
            "Drive Direction(FWD/REV/NEUTRAL)",
            "Drive Mode",
        ]
        
        for r, label in enumerate(right_rows):
            self.create_table_row(right_container, r, label, width1=380, width2=200)
    
    def create_speed_loop_tab(self):
        """Create Speed Loop PI Gains tab content"""
        tab = self.tabs["Speed Loop\nPI Gains"]
        
        # Table container
        table_container = ctk.CTkFrame(tab, fg_color="#F7F7F7")
        table_container.pack(padx=20, pady=20, anchor="w")
        
        # Create table
        table_frame = ctk.CTkFrame(table_container, fg_color="white", corner_radius=0)
        table_frame.pack()
        
        # Define rows
        rows = [
            "Speed Loop Kp",
            "Speed Loop Ki",
        ]
        
        # Create table rows
        for r, label in enumerate(rows):
            self.create_table_row(table_frame, r, label)
        
        # Column widths
        table_frame.grid_columnconfigure(0, minsize=320)
        table_frame.grid_columnconfigure(1, minsize=220)
    
    def create_thermal_status_tab(self):
        """Create Thermal Status tab content"""
        tab = self.tabs["Thermal\nStatus"]
        
        # Main container
        main_frame = ctk.CTkFrame(tab, fg_color="#F7F7F7")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Top section - Drive Monitoring Signals (left) and Inverter Thresholds (right)
        top_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        top_frame.pack(fill="x", pady=(0, 20))
        
        # Left: Drive Monitoring Signals
        left_top = ctk.CTkFrame(top_frame, fg_color="white", corner_radius=0)
        left_top.grid(row=0, column=0, padx=(0, 20), sticky="nw")
        
        drive_rows = [
            "Actual Speed(RPM)",
            "Reference Speed(RPM)",
            "Reference Torque(RPM)",
            "Max Speed Limit(RPM)",
            "Encoder Count",
        ]
        
        for r, label in enumerate(drive_rows):
            self.create_table_row(left_top, r, label, width1=280, width2=160)
        
        # Right: Inverter Thresholds
        right_top = ctk.CTkFrame(top_frame, fg_color="white", corner_radius=0)
        right_top.grid(row=0, column=1, sticky="nw")
        
        # Inverter header
        inv_header = ctk.CTkFrame(right_top, fg_color="#FFFFFF", corner_radius=0, 
                                  border_width=1, border_color="#CFCFCF")
        inv_header.grid(row=0, column=0, columnspan=2, sticky="ew")
        ctk.CTkLabel(
            inv_header, text="Inverter Thresholds", 
            text_color="#2D2D2D", font=ctk.CTkFont(size=13, weight="bold")
        ).pack(padx=14, pady=10)
        
        inverter_rows = [
            "Inverter Temp Limit 1(°C)",
            "Inverter Temp Limit 2(°C)",
            "Inverter Temp Limit 2(°C)",
        ]
        
        for r, label in enumerate(inverter_rows, start=1):
            self.create_table_row(right_top, r, label, width1=280, width2=160, 
                                 row_color="#E6F2EA" if r % 2 == 0 else "#FFFFFF")
        
        # Bottom section - Controller Thresholds (left) and Motor Thresholds (right)
        bottom_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        bottom_frame.pack(fill="x")
        
        # Left: Controller Thresholds
        left_bottom = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=0)
        left_bottom.grid(row=0, column=0, padx=(0, 20), sticky="nw")
        
        # Controller header
        ctrl_header = ctk.CTkFrame(left_bottom, fg_color="#FFFFFF", corner_radius=0,
                                   border_width=1, border_color="#CFCFCF")
        ctrl_header.grid(row=0, column=0, columnspan=2, sticky="ew")
        ctk.CTkLabel(
            ctrl_header, text="Controller Thresholds",
            text_color="#2D2D2D", font=ctk.CTkFont(size=13, weight="bold")
        ).pack(padx=14, pady=10)
        
        controller_rows = [
            "Controller Temp Limit 1(°C)",
            "Controller Temp Limit 2(°C)",
            "Controller Temp Limit 3(°C)",
        ]
        
        for r, label in enumerate(controller_rows, start=1):
            self.create_table_row(left_bottom, r, label, width1=280, width2=160,
                                 row_color="#E6F2EA" if r % 2 == 0 else "#FFFFFF")
        
        # Right: Motor Thresholds
        right_bottom = ctk.CTkFrame(bottom_frame, fg_color="white", corner_radius=0)
        right_bottom.grid(row=0, column=1, sticky="nw")
        
        # Motor header
        motor_header = ctk.CTkFrame(right_bottom, fg_color="#FFFFFF", corner_radius=0,
                                    border_width=1, border_color="#CFCFCF")
        motor_header.grid(row=0, column=0, columnspan=2, sticky="ew")
        ctk.CTkLabel(
            motor_header, text="Motor Thresholds",
            text_color="#2D2D2D", font=ctk.CTkFont(size=13, weight="bold")
        ).pack(padx=14, pady=10)
        
        motor_rows = [
            "Motor Temp Limit 1(°C)",
            "Motor Temp Limit 2(°C)",
            "Motor Temp Limit 3(°C)",
        ]
        
        for r, label in enumerate(motor_rows, start=1):
            self.create_table_row(right_bottom, r, label, width1=280, width2=160,
                                 row_color="#E6F2EA" if r % 2 == 0 else "#FFFFFF")
    
    def create_can_communication_tab(self):
        """Create Can Communication Status tab content"""
        tab = self.tabs["Can Communication\nStatus"]
        
        # Table container
        table_container = ctk.CTkFrame(tab, fg_color="#F7F7F7")
        table_container.pack(padx=20, pady=20, anchor="w")
        
        # Create table
        table_frame = ctk.CTkFrame(table_container, fg_color="white", corner_radius=0)
        table_frame.pack()
        
        # Define rows
        rows = [
            "CAN Timeout",
            "Counter",
        ]
        
        # Create table rows
        for r, label in enumerate(rows):
            self.create_table_row(table_frame, r, label)
        
        # Column widths
        table_frame.grid_columnconfigure(0, minsize=320)
        table_frame.grid_columnconfigure(1, minsize=220)
    
    def create_table_row(self, parent, row_num, label, width1=320, width2=220, row_color=None):
        """Create a single table row with label and value cells"""
        # Left label cell
        left = ctk.CTkFrame(
            parent, fg_color="#FFFFFF", corner_radius=0,
            border_width=1, border_color="#CFCFCF"
        )
        left.grid(row=row_num, column=0, sticky="nsew")
        ctk.CTkLabel(
            left, text=label, text_color="#2D2D2D",
            font=ctk.CTkFont(size=13)
        ).pack(padx=14, pady=10, anchor="w")
        
        # Right value cell (alternate mint background)
        if row_color is None:
            bg = "#E6F2EA" if row_num % 2 == 1 else "#FFFFFF"
        else:
            bg = row_color
        right = ctk.CTkFrame(
            parent, fg_color=bg, corner_radius=0,
            border_width=1, border_color="#CFCFCF"
        )
        right.grid(row=row_num, column=1, sticky="nsew")
        ctk.CTkLabel(right, text="", text_color="#2D2D2D").pack(
            padx=14, pady=10, anchor="w"
        )
        
        # Column widths
        parent.grid_columnconfigure(0, minsize=width1)
        parent.grid_columnconfigure(1, minsize=width2)
