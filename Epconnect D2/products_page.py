import customtkinter as ctk


class ProductsPage:
    """Products page with Motor Family, Motor Series, and Motor Info sections"""
    
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.create_products_page()
    
    def create_products_page(self):
        """Create the Products page layout"""
        # Main container with two columns
        main_container = ctk.CTkFrame(self.parent_frame, fg_color="#F5F5F5")
        main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Configure grid layout
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(1, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        # Left panel - Motor Family and Motor Series (Purple background)
        left_panel = ctk.CTkFrame(main_container, fg_color="#B8B3D4", corner_radius=10)
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=0)
        
        # Motor Family section
        self.create_motor_family_section(left_panel)
        
        # Motor Series section
        self.create_motor_series_section(left_panel)
        
        # Right panel - Motor Info (Light gray background)
        right_panel = ctk.CTkFrame(main_container, fg_color="#E8E8E8", corner_radius=10)
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=0)
        
        # Motor Info section
        self.create_motor_info_section(right_panel)
    
    def create_motor_family_section(self, parent):
        """Create the Motor Family search section"""
        # Title
        title = ctk.CTkLabel(
            parent,
            text="Motor Family",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        title.pack(pady=(30, 20), padx=20)
        
        # Search box
        self.motor_family_search = ctk.CTkEntry(
            parent,
            placeholder_text="Searching",
            height=50,
            width=450,
            corner_radius=25,
            fg_color="white",
            border_width=0,
            font=ctk.CTkFont(size=16),
            text_color="#999999"
        )
        self.motor_family_search.pack(pady=(0, 40), padx=40)
    
    def create_motor_series_section(self, parent):
        """Create the Motor Series search section"""
        # Title
        title = ctk.CTkLabel(
            parent,
            text="Motor Series",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        title.pack(pady=(20, 20), padx=20)
        
        # Search box
        self.motor_series_search = ctk.CTkEntry(
            parent,
            placeholder_text="Searching",
            height=50,
            width=450,
            corner_radius=25,
            fg_color="white",
            border_width=0,
            font=ctk.CTkFont(size=16),
            text_color="#999999"
        )
        self.motor_series_search.pack(pady=(0, 40), padx=40)
    
    def create_motor_info_section(self, parent):
        """Create the Motor Info table section"""
        # Title
        title = ctk.CTkLabel(
            parent,
            text="Motor Info",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2D2D2D"
        )
        title.pack(pady=(30, 20))
        
        # Info table container
        table_container = ctk.CTkFrame(parent, fg_color="#E8E8E8")
        table_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Motor info fields with labels and values
        motor_info_fields = [
            ("Motor Model", "?"),
            ("Motor Type", "-"),
            ("Motor Version", "-"),
            ("Housing Version", "-"),
            ("Pole Pairs", "-"),
            ("Phase Resistance(R)", "mohm"),
            ("Flux Linkage", "mWb"),
            ("D axis Inductance(Ld)", "mH"),
            ("Q axis Inductance(Lq)", "mH"),
            ("Peak Torque", "Nm"),
            ("Related Torque", "Nm"),
            ("Peak Power Rating", "Kw"),
            ("Continuous Power rating", "Kw"),
        ]
        
        for idx, (label, value) in enumerate(motor_info_fields):
            # Create row frame
            row_frame = ctk.CTkFrame(
                table_container,
                fg_color="#B8B3D4",
                corner_radius=0,
                border_width=1,
                border_color="#9999AA"
            )
            row_frame.pack(fill="x", pady=1)
            
            # Configure grid
            row_frame.grid_columnconfigure(0, weight=1)
            row_frame.grid_columnconfigure(1, weight=0)
            
            # Label
            label_widget = ctk.CTkLabel(
                row_frame,
                text=label,
                font=ctk.CTkFont(size=14),
                text_color="#2D2D2D",
                anchor="w"
            )
            label_widget.grid(row=0, column=0, sticky="w", padx=15, pady=12)
            
            # Value
            value_widget = ctk.CTkLabel(
                row_frame,
                text=value,
                font=ctk.CTkFont(size=14),
                text_color="#2D2D2D",
                anchor="e"
            )
            value_widget.grid(row=0, column=1, sticky="e", padx=15, pady=12)
