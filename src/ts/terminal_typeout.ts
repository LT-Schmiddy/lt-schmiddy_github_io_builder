require("jquery");

class TerminalTypeoutController {
    elem: HTMLElement;
    text: string;
    typing_interval: number;
    on_complete: Function | null;

    private add_pos: number = 0;

    constructor(p_typeout_elem: HTMLElement, p_typing_interval: number = 100, p_on_complete: Function | null = null) {
        this.elem = p_typeout_elem;
        this.text = this.elem.innerText;
        this.typing_interval = p_typing_interval;
        this.on_complete = p_on_complete;

        console.log(this.text);
        this.elem.innerText = "";
        setTimeout(()=>{this.update()}, this.typing_interval);
    }

    update() {
        if (this.add_pos === this.text.length) {
            this.elem.innerHTML = this.text;
            if (this.on_complete !== null) {
                this.on_complete();
            }
        } else {
            this.elem.innerText += this.text.charAt(this.add_pos);
            this.add_pos++;
            setTimeout(()=>{this.update()}, this.typing_interval);
        }
    }
}

class BlinkController {
    elem: HTMLElement;
    text: string;
    interval: number;

    private is_visible: boolean = true;
    constructor(p_elem: HTMLElement, p_interval: number = 1000, start_now: boolean = true) {
        this.elem = p_elem;
        this.text = this.elem.innerText;
        this.interval = p_interval;

        if (start_now) {
            this.update();
        }
    }

    update() {
        if (this.is_visible) {
            this.elem.innerHTML = this.text;
        } else {
            this.elem.innerHTML = "";
        }
        this.is_visible = !this.is_visible;
        setTimeout(()=>{this.update()}, this.interval);
    }
}

var term_type_controllers: Array<TerminalTypeoutController> = [];

$(()=>{
    let tt_items = $(".terminal-typeout");
    for (let i = 0; i < tt_items.length; i++) {
        let item = tt_items.get(i);
        term_type_controllers.push(new TerminalTypeoutController(<HTMLElement>item));
    }

    // Handling header:
    let header_typeout = $("#header-typeout");
    let header_blink = $("#header-blink");

    let header_blink_controller = new BlinkController(<HTMLElement>header_blink.get(0), 700, false);
    term_type_controllers.push(new TerminalTypeoutController(<HTMLElement>header_typeout.get(0), 100, ()=>{header_blink_controller.update()}));
})