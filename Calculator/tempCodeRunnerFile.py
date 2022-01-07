def positive_negative(self):
        prev_number=self.ids.input_box.text
        
        if "-" in prev_number:
            self.ids.input_box.text=f"{prev_number.replace('-','')}"

        else:
            self.ids.input_box.text=f"-{prev_number}"