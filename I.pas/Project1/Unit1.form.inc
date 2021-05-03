procedure InitializeComponent;
    begin
        self.button1 := new System.Windows.Forms.Button();
        self.textBox1 := new System.Windows.Forms.TextBox();
        self.textBox2 := new System.Windows.Forms.TextBox();
        self.SuspendLayout();
        // 
        // button1
        // 
        self.button1.BackColor := System.Drawing.Color.FromArgb((System.Int32((System.Byte(217)))), (System.Int32((System.Byte(217)))), (System.Int32((System.Byte(217)))));
        self.button1.FlatAppearance.BorderSize := 0;
        self.button1.FlatStyle := System.Windows.Forms.FlatStyle.Flat;
        self.button1.ForeColor := System.Drawing.Color.Black;
        self.button1.Location := new System.Drawing.Point(0, 0);
        self.button1.Name := 'button1';
        self.button1.Size := new System.Drawing.Size(62, 21);
        self.button1.TabIndex := 0;
        self.button1.Text := 'button1';
        self.button1.UseVisualStyleBackColor := false;
        // 
        // textBox1
        // 
        self.textBox1.Cursor := System.Windows.Forms.Cursors.IBeam;
        self.textBox1.Font := new System.Drawing.Font('Arial', 10);
        self.textBox1.ForeColor := System.Drawing.Color.Black;
        self.textBox1.Location := new System.Drawing.Point(62, 0);
        self.textBox1.Name := 'textBox1';
        self.textBox1.Size := new System.Drawing.Size(734, 23);
        self.textBox1.TabIndex := 1;
        // 
        // textBox2
        // 
        self.textBox2.BorderStyle := System.Windows.Forms.BorderStyle.FixedSingle;
        self.textBox2.Font := new System.Drawing.Font('Consolas', 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.textBox2.Location := new System.Drawing.Point(0, 21);
        self.textBox2.Multiline := true;
        self.textBox2.Name := 'textBox2';
        self.textBox2.Size := new System.Drawing.Size(746, 423);
        self.textBox2.TabIndex := 2;
        // 
        // form
        // 
        self.BackColor := System.Drawing.Color.White;
        self.ClientSize := new System.Drawing.Size(746, 444);
        self.Controls.Add(self.textBox2);
        self.Controls.Add(self.textBox1);
        self.Controls.Add(self.button1);
        self.ForeColor := System.Drawing.SystemColors.ControlText;
        self.Name := 'form';
        self.Text := 'Form1';
        self.Load += Form1_Load;
        self.Resize += Form1_Resize;
        self.ResumeLayout(false);
        self.PerformLayout();
    end;
