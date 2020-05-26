from typing import Tuple
from pyglet import gl
from ctypes import byref
import weakref


class Texture:
    def __init__(self, size: Tuple[int, int], component: int, data):
        self.width, self.height = size
        sized_format = (gl.GL_R8, gl.GL_RG8, gl.GL_RGB8, gl.GL_RGBA8)[component - 1]
        self.format = (gl.GL_R, gl.GL_RG, gl.GL_RGB, gl.GL_RGBA)[component - 1]
        gl.glActiveTexture(gl.GL_TEXTURE0 + 0)  # If we need other texture unit...
        self.texture_id = texture_id = gl.GLuint()
        gl.glGenTextures(1, byref(self.texture_id))

        if self.texture_id.value == 0:
            raise ShaderException("Cannot create Texture.")

        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)
        gl.glPixelStorei(gl.GL_PACK_ALIGNMENT, 1)
        gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
        try:
            gl.glTexImage2D(
                gl.GL_TEXTURE_2D, 0, sized_format, self.width, self.height, 0,
                self.format, gl.GL_UNSIGNED_BYTE, data
            )
        except gl.GLException:
            raise gl.GLException(f"Unable to create texture. {gl.GL_MAX_TEXTURE_SIZE} {size}")

        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        weakref.finalize(self, Texture.release, texture_id)

    @staticmethod
    def release(texture_id):
        # If we have no context, then we are shutting down, so skip this
        if gl.current_context is None:
            return

        if texture_id.value != 0:
            gl.glDeleteTextures(1, byref(texture_id))

    def use(self, texture_unit: int = 0):
        gl.glActiveTexture(gl.GL_TEXTURE0 + texture_unit)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)



import arcade.shader

print("Monkeypatch arcade.shader.Texture " + str(hex(id(arcade.shader.Texture))))

arcade.shader.Texture = Texture

print("Monkeypatch complete "+ str(hex(id(arcade.shader.Texture))))