procedure InitializeComponent;
    begin
        var resources: System.ComponentModel.ComponentResourceManager := new System.ComponentModel.ComponentResourceManager(typeof(Form1));
        self.label7 := new System.Windows.Forms.Label();
        self.listBox2 := new System.Windows.Forms.ListBox();
        self.linkLabel1 := new System.Windows.Forms.LinkLabel();
        self.button4 := new System.Windows.Forms.Button();
        self.groupBox1 := new System.Windows.Forms.GroupBox();
        self.label9 := new System.Windows.Forms.Label();
        self.download := new System.Windows.Forms.TextBox();
        self.label8 := new System.Windows.Forms.Label();
        self.website := new System.Windows.Forms.TextBox();
        self.label6 := new System.Windows.Forms.Label();
        self.description := new System.Windows.Forms.RichTextBox();
        self.status := new System.Windows.Forms.TextBox();
        self.filename := new System.Windows.Forms.TextBox();
        self.version := new System.Windows.Forms.TextBox();
        self.author := new System.Windows.Forms.TextBox();
        self.label5 := new System.Windows.Forms.Label();
        self.label4 := new System.Windows.Forms.Label();
        self.label3 := new System.Windows.Forms.Label();
        self.label2 := new System.Windows.Forms.Label();
        self.label1 := new System.Windows.Forms.Label();
        self.button2 := new System.Windows.Forms.Button();
        self.ListBox1 := new System.Windows.Forms.CheckedListBox();
        self.button1 := new System.Windows.Forms.Button();
        self.button3 := new System.Windows.Forms.Button();
        self.button9 := new System.Windows.Forms.Button();
        self.button10 := new System.Windows.Forms.Button();
        self.button11 := new System.Windows.Forms.Button();
        self.button5 := new System.Windows.Forms.Button();
        self.button6 := new System.Windows.Forms.Button();
        self.button7 := new System.Windows.Forms.Button();
        self.button8 := new System.Windows.Forms.Button();
        self.button12 := new System.Windows.Forms.Button();
        self.listbox2_focus := new System.Windows.Forms.TextBox();
        self.groupBox1.SuspendLayout();
        self.SuspendLayout();
        // 
        // label7
        // 
        self.label7.Font := new System.Drawing.Font('Segoe UI Emoji', 12);
        self.label7.Location := new System.Drawing.Point(907, 2);
        self.label7.Name := 'label7';
        self.label7.Size := new System.Drawing.Size(187, 23);
        self.label7.TabIndex := 21;
        self.label7.Text := 'selected mod order';
        // 
        // listBox2
        // 
        self.listBox2.Font := new System.Drawing.Font('Microsoft Sans Serif', 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.listBox2.FormattingEnabled := true;
        self.listBox2.ItemHeight := 18;
        self.listBox2.Location := new System.Drawing.Point(829, 30);
        self.listBox2.Name := 'listBox2';
        self.listBox2.SelectionMode := System.Windows.Forms.SelectionMode.MultiSimple;
        self.listBox2.Size := new System.Drawing.Size(269, 328);
        self.listBox2.TabIndex := 1;
        self.listBox2.MouseClick += listBox2_MouseClick;
        self.listBox2.SelectedIndexChanged += listBox2_SelectedIndexChanged;
        self.listBox2.Enter += listBox2_Enter;
        self.listBox2.KeyDown += listBox2_KeyDown;
        // 
        // linkLabel1
        // 
        self.linkLabel1.Font := new System.Drawing.Font('Segoe UI Emoji', 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(0)));
        self.linkLabel1.LinkBehavior := System.Windows.Forms.LinkBehavior.NeverUnderline;
        self.linkLabel1.LinkColor := System.Drawing.Color.Black;
        self.linkLabel1.Location := new System.Drawing.Point(11, 2);
        self.linkLabel1.Name := 'linkLabel1';
        self.linkLabel1.Size := new System.Drawing.Size(89, 26);
        self.linkLabel1.TabIndex := 12;
        self.linkLabel1.TabStop := true;
        self.linkLabel1.Text := 'mods';
        self.linkLabel1.TextAlign := System.Drawing.ContentAlignment.TopCenter;
        // 
        // button4
        // 
        self.button4.Image := (System.Drawing.Image(resources.GetObject('button4.Image')));
        self.button4.Location := new System.Drawing.Point(177, 364);
        self.button4.Name := 'button4';
        self.button4.Size := new System.Drawing.Size(49, 36);
        self.button4.TabIndex := 5;
        self.button4.UseVisualStyleBackColor := false;
        self.button4.Click += button4_Click;
        // 
        // groupBox1
        // 
        self.groupBox1.Controls.Add(self.label9);
        self.groupBox1.Controls.Add(self.download);
        self.groupBox1.Controls.Add(self.label8);
        self.groupBox1.Controls.Add(self.website);
        self.groupBox1.Controls.Add(self.label6);
        self.groupBox1.Controls.Add(self.description);
        self.groupBox1.Controls.Add(self.status);
        self.groupBox1.Controls.Add(self.filename);
        self.groupBox1.Controls.Add(self.version);
        self.groupBox1.Controls.Add(self.author);
        self.groupBox1.Controls.Add(self.label5);
        self.groupBox1.Controls.Add(self.label4);
        self.groupBox1.Controls.Add(self.label3);
        self.groupBox1.Controls.Add(self.label2);
        self.groupBox1.Controls.Add(self.label1);
        self.groupBox1.Location := new System.Drawing.Point(287, 9);
        self.groupBox1.Name := 'groupBox1';
        self.groupBox1.Size := new System.Drawing.Size(535, 391);
        self.groupBox1.TabIndex := 21;
        self.groupBox1.TabStop := false;
        // 
        // label9
        // 
        self.label9.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label9.Location := new System.Drawing.Point(53, 310);
        self.label9.Name := 'label9';
        self.label9.Size := new System.Drawing.Size(98, 23);
        self.label9.TabIndex := 27;
        self.label9.Text := 'download';
        // 
        // download
        // 
        self.download.BackColor := System.Drawing.Color.White;
        self.download.Font := new System.Drawing.Font('Verdana', 9);
        self.download.Location := new System.Drawing.Point(6, 336);
        self.download.Name := 'download';
        self.download.ReadOnly := true;
        self.download.Size := new System.Drawing.Size(259, 26);
        self.download.TabIndex := 18;
        self.download.DoubleClick += download_DoubleClick;
        // 
        // label8
        // 
        self.label8.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label8.Location := new System.Drawing.Point(53, 253);
        self.label8.Name := 'label8';
        self.label8.Size := new System.Drawing.Size(98, 23);
        self.label8.TabIndex := 26;
        self.label8.Text := 'website';
        // 
        // website
        // 
        self.website.BackColor := System.Drawing.Color.White;
        self.website.Font := new System.Drawing.Font('Verdana', 9);
        self.website.Location := new System.Drawing.Point(6, 279);
        self.website.Name := 'website';
        self.website.ReadOnly := true;
        self.website.Size := new System.Drawing.Size(259, 26);
        self.website.TabIndex := 17;
        self.website.DoubleClick += website_DoubleClick;
        // 
        // label6
        // 
        self.label6.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label6.Location := new System.Drawing.Point(341, 28);
        self.label6.Name := 'label6';
        self.label6.Size := new System.Drawing.Size(128, 23);
        self.label6.TabIndex := 28;
        self.label6.Text := 'description';
        // 
        // description
        // 
        self.description.BackColor := System.Drawing.Color.White;
        self.description.Font := new System.Drawing.Font('Lucida Sans Unicode', 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.description.Location := new System.Drawing.Point(271, 54);
        self.description.Name := 'description';
        self.description.ReadOnly := true;
        self.description.Size := new System.Drawing.Size(252, 319);
        self.description.TabIndex := 19;
        self.description.Text := '';
        // 
        // status
        // 
        self.status.BackColor := System.Drawing.Color.White;
        self.status.Font := new System.Drawing.Font('Verdana', 9);
        self.status.Location := new System.Drawing.Point(6, 222);
        self.status.Name := 'status';
        self.status.ReadOnly := true;
        self.status.Size := new System.Drawing.Size(259, 26);
        self.status.TabIndex := 16;
        // 
        // filename
        // 
        self.filename.BackColor := System.Drawing.Color.White;
        self.filename.Font := new System.Drawing.Font('Verdana', 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.filename.Location := new System.Drawing.Point(6, 54);
        self.filename.Name := 'filename';
        self.filename.ReadOnly := true;
        self.filename.Size := new System.Drawing.Size(259, 26);
        self.filename.TabIndex := 13;
        // 
        // version
        // 
        self.version.BackColor := System.Drawing.Color.White;
        self.version.Font := new System.Drawing.Font('Verdana', 9);
        self.version.Location := new System.Drawing.Point(6, 166);
        self.version.Name := 'version';
        self.version.ReadOnly := true;
        self.version.Size := new System.Drawing.Size(259, 26);
        self.version.TabIndex := 15;
        // 
        // author
        // 
        self.author.BackColor := System.Drawing.Color.White;
        self.author.Font := new System.Drawing.Font('Verdana', 9);
        self.author.Location := new System.Drawing.Point(6, 110);
        self.author.Name := 'author';
        self.author.ReadOnly := true;
        self.author.Size := new System.Drawing.Size(259, 26);
        self.author.TabIndex := 14;
        // 
        // label5
        // 
        self.label5.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label5.Location := new System.Drawing.Point(53, 196);
        self.label5.Name := 'label5';
        self.label5.Size := new System.Drawing.Size(98, 23);
        self.label5.TabIndex := 25;
        self.label5.Text := 'status';
        // 
        // label4
        // 
        self.label4.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label4.Location := new System.Drawing.Point(53, 140);
        self.label4.Name := 'label4';
        self.label4.Size := new System.Drawing.Size(98, 23);
        self.label4.TabIndex := 24;
        self.label4.Text := 'version';
        // 
        // label3
        // 
        self.label3.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label3.Location := new System.Drawing.Point(53, 28);
        self.label3.Name := 'label3';
        self.label3.Size := new System.Drawing.Size(98, 23);
        self.label3.TabIndex := 22;
        self.label3.Text := 'filename';
        // 
        // label2
        // 
        self.label2.Font := new System.Drawing.Font('Sitka Small', 10.2, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.label2.Location := new System.Drawing.Point(53, 84);
        self.label2.Name := 'label2';
        self.label2.Size := new System.Drawing.Size(98, 23);
        self.label2.TabIndex := 23;
        self.label2.Text := 'author';
        // 
        // label1
        // 
        self.label1.Font := new System.Drawing.Font('Segoe UI Emoji', 12);
        self.label1.Location := new System.Drawing.Point(164, -7);
        self.label1.Name := 'label1';
        self.label1.Size := new System.Drawing.Size(168, 23);
        self.label1.TabIndex := 20;
        self.label1.Text := 'selected mod info';
        // 
        // button2
        // 
        self.button2.Image := (System.Drawing.Image(resources.GetObject('button2.Image')));
        self.button2.Location := new System.Drawing.Point(67, 364);
        self.button2.Name := 'button2';
        self.button2.Size := new System.Drawing.Size(49, 36);
        self.button2.TabIndex := 3;
        self.button2.UseVisualStyleBackColor := false;
        self.button2.Click += button2_Click;
        // 
        // ListBox1
        // 
        self.ListBox1.CheckOnClick := true;
        self.ListBox1.Font := new System.Drawing.Font('Microsoft Sans Serif', 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, (System.Byte(204)));
        self.ListBox1.FormattingEnabled := true;
        self.ListBox1.HorizontalScrollbar := true;
        self.ListBox1.Location := new System.Drawing.Point(12, 31);
        self.ListBox1.Name := 'ListBox1';
        self.ListBox1.Size := new System.Drawing.Size(269, 327);
        self.ListBox1.TabIndex := 0;
        self.ListBox1.ItemCheck += ListBox1_ItemCheck;
        self.ListBox1.SelectedIndexChanged += ListBox1_SelectedIndexChanged;
        self.ListBox1.Enter += ListBox1_Enter;
        self.ListBox1.Leave += ListBox1_Leave;
        // 
        // button1
        // 
        self.button1.Image := (System.Drawing.Image(resources.GetObject('button1.Image')));
        self.button1.Location := new System.Drawing.Point(12, 364);
        self.button1.Name := 'button1';
        self.button1.Size := new System.Drawing.Size(49, 36);
        self.button1.TabIndex := 2;
        self.button1.UseVisualStyleBackColor := false;
        self.button1.Click += button1_Click;
        // 
        // button3
        // 
        self.button3.Image := (System.Drawing.Image(resources.GetObject('button3.Image')));
        self.button3.Location := new System.Drawing.Point(122, 364);
        self.button3.Name := 'button3';
        self.button3.Size := new System.Drawing.Size(49, 36);
        self.button3.TabIndex := 4;
        self.button3.UseVisualStyleBackColor := false;
        self.button3.Click += button3_Click;
        // 
        // button9
        // 
        self.button9.Location := new System.Drawing.Point(238, 369);
        self.button9.Name := 'button9';
        self.button9.Size := new System.Drawing.Size(51, 36);
        self.button9.TabIndex := 6;
        self.button9.UseVisualStyleBackColor := true;
        // 
        // button10
        // 
        self.button10.Location := new System.Drawing.Point(945, 369);
        self.button10.Name := 'button10';
        self.button10.Size := new System.Drawing.Size(51, 36);
        self.button10.TabIndex := 9;
        self.button10.UseVisualStyleBackColor := true;
        // 
        // button11
        // 
        self.button11.Image := (System.Drawing.Image(resources.GetObject('button11.Image')));
        self.button11.Location := new System.Drawing.Point(232, 364);
        self.button11.Name := 'button11';
        self.button11.Size := new System.Drawing.Size(49, 36);
        self.button11.TabIndex := 6;
        self.button11.UseVisualStyleBackColor := false;
        self.button11.Click += button11_Click;
        // 
        // button5
        // 
        self.button5.Image := (System.Drawing.Image(resources.GetObject('button5.Image')));
        self.button5.Location := new System.Drawing.Point(1049, 364);
        self.button5.Name := 'button5';
        self.button5.Size := new System.Drawing.Size(49, 36);
        self.button5.TabIndex := 11;
        self.button5.UseVisualStyleBackColor := false;
        self.button5.Click += button5_Click;
        // 
        // button6
        // 
        self.button6.Image := (System.Drawing.Image(resources.GetObject('button6.Image')));
        self.button6.Location := new System.Drawing.Point(994, 364);
        self.button6.Name := 'button6';
        self.button6.Size := new System.Drawing.Size(49, 36);
        self.button6.TabIndex := 10;
        self.button6.UseVisualStyleBackColor := false;
        self.button6.Click += button6_Click;
        // 
        // button7
        // 
        self.button7.Image := (System.Drawing.Image(resources.GetObject('button7.Image')));
        self.button7.Location := new System.Drawing.Point(884, 364);
        self.button7.Name := 'button7';
        self.button7.Size := new System.Drawing.Size(49, 36);
        self.button7.TabIndex := 8;
        self.button7.UseVisualStyleBackColor := false;
        self.button7.Click += button7_Click;
        // 
        // button8
        // 
        self.button8.Image := (System.Drawing.Image(resources.GetObject('button8.Image')));
        self.button8.Location := new System.Drawing.Point(829, 364);
        self.button8.Name := 'button8';
        self.button8.Size := new System.Drawing.Size(49, 36);
        self.button8.TabIndex := 7;
        self.button8.UseVisualStyleBackColor := false;
        self.button8.Click += button8_Click;
        // 
        // button12
        // 
        self.button12.Image := (System.Drawing.Image(resources.GetObject('button12.Image')));
        self.button12.Location := new System.Drawing.Point(939, 364);
        self.button12.Name := 'button12';
        self.button12.Size := new System.Drawing.Size(49, 36);
        self.button12.TabIndex := 9;
        self.button12.UseVisualStyleBackColor := false;
        self.button12.Click += button12_Click;
        // 
        // listbox2_focus
        // 
        self.listbox2_focus.Location := new System.Drawing.Point(122, 2);
        self.listbox2_focus.Multiline := true;
        self.listbox2_focus.Name := 'listbox2_focus';
        self.listbox2_focus.ReadOnly := true;
        self.listbox2_focus.Size := new System.Drawing.Size(1, 1);
        self.listbox2_focus.TabIndex := 29;
        self.listbox2_focus.Enter += listbox2_focus_Enter;
        self.listbox2_focus.KeyDown += listbox2_focus_KeyDown;
        self.listbox2_focus.Leave += listbox2_focus_Leave;
        // 
        // Form1
        // 
        self.BackColor := System.Drawing.Color.White;
        self.ClientSize := new System.Drawing.Size(1113, 413);
        self.Controls.Add(self.listbox2_focus);
        self.Controls.Add(self.button5);
        self.Controls.Add(self.button6);
        self.Controls.Add(self.button7);
        self.Controls.Add(self.button8);
        self.Controls.Add(self.button12);
        self.Controls.Add(self.button11);
        self.Controls.Add(self.label7);
        self.Controls.Add(self.listBox2);
        self.Controls.Add(self.linkLabel1);
        self.Controls.Add(self.button4);
        self.Controls.Add(self.groupBox1);
        self.Controls.Add(self.button2);
        self.Controls.Add(self.ListBox1);
        self.Controls.Add(self.button1);
        self.Controls.Add(self.button3);
        self.Font := new System.Drawing.Font('Verdana', 10.2);
        self.HelpButton := true;
        self.Icon := (System.Drawing.Icon(resources.GetObject('$this.Icon')));
        self.MaximumSize := new System.Drawing.Size(1131, 460);
        self.MinimumSize := new System.Drawing.Size(1131, 460);
        self.Name := 'Form1';
        self.StartPosition := System.Windows.Forms.FormStartPosition.CenterScreen;
        self.Text := 'ModLauncher';
        self.Load += Form1_Load;
        self.groupBox1.ResumeLayout(false);
        self.groupBox1.PerformLayout();
        self.ResumeLayout(false);
        self.PerformLayout();
    end;
