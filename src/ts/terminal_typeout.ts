require("jquery");

class TerminalTypeoutController {
    elem: HTMLElement;
    text: string;
    typing_interval: number;
    cursor_char: string = "|";

    private add_pos: number = 0;

    constructor(p_elem: HTMLElement, p_typing_interval: number = 100) {
        this.elem = p_elem;
        this.text = this.elem.innerText;
        this.typing_interval = p_typing_interval;

        console.log(this.text);
        this.elem.innerText = "";
        setTimeout(()=>{this.update()}, this.typing_interval);
    }

    update() {
        if (this.add_pos === this.text.length) {
            this.elem.innerHTML = this.text;
        } else {
            this.elem.innerText += this.text.charAt(this.add_pos);
            this.add_pos++;
            setTimeout(()=>{this.update()}, this.typing_interval);
        }
    }
}

var term_type_controllers: Array<TerminalTypeoutController> = [];

$(()=>{
    let tt_items = $(".terminal-typeout");
    for (let i = 0; i < tt_items.length; i++) {
        let item = tt_items.get(i);
        term_type_controllers.push(new TerminalTypeoutController(<HTMLElement>item));
    }
})