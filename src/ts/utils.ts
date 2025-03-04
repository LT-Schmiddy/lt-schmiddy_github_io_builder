export function expose_on_window(name: string, item: any) {
    let w_any = <any>window;
    w_any[name] = item;
}
