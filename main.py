from properties import *
import moderngl as mgl
import pygame as pg
import sys
from shader_program import ShaderProgram


class VoxelGame:
    def __init__(self):
        self.shader_program = None
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(window_resolution, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto"

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.shader_program = ShaderProgram(self)

    def update(self):
        self.shader_program.update()

        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() / 1000
        pg.display.set_caption(f"{window_title} | FPS: {self.clock.get_fps()}")

    def render(self):
        self.ctx.clear()
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
                pg.quit()
                sys.exit()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    game = VoxelGame()
    game.run()
