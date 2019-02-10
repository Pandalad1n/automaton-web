export default class Renderer {
    constructor (canvasElement, field) {
        this.element = canvasElement
        this.field = field
    }

    start () {
        this.isRunning = true
        this.nextFrame()
    }

    stop () {
        this.isRunning = false
    }

    render () {
        this.element.width = this.element.clientWidth
        this.element.height = this.element.clientHeight
        const ctx = this.element.getContext('2d')
        ctx.fillStyle = "#00897b"

        let height = this.element.clientHeight / this.field.height()
        let width = this.element.clientWidth / this.field.width()
        for (let y in this.field.data) {
            for (let x in this.field.data[y]) {
                if(this.field.data[y][x]) {
                    ctx.fillRect(x*width, y*height, width, height)
                }
            }
        }

        this.nextFrame()
    }

    nextFrame () {
        window.requestAnimationFrame(this.render.bind(this))
    }
}