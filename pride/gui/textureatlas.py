#dont_cache flag on objects that are too large

import pride.components.base

class Texture_Atlas(pride.components.base.Base):

    defaults = {"chunk_sizes" : [(8 * (2 ** x), 8 * (2 ** x)) for x in range(8)],
                'h' : 2048, 'w' : 2048, 'x' : 2048, 'y' : 2048}
    mutable_defaults = {"offsets" : dict, "grid_position" : dict, "unused" : dict}

    def __init__(self, **kwargs):
        super(Texture_Atlas, self).__init__(**kwargs)
        max_size = self.max_size = sorted(self.chunk_sizes)[-1]
        self.rows = [[] for row_number in range(self.h / max_size[0])]

    def add_to_atlas(self, identifier, area):
        # storage
        # find the next rect that is >= area
        # rects stored in rows
        # store rect in left-most position on first row that it fits in
        #   - if it can't fit on one row, then go to/make a new one
        # map identifier in grid_position to (row, position)
        # map identifier in offset to (x_offset, y_offset)
        #
        # retrieval
        # return (x_offset, y_offset) from offset[identifier]
        chunk_size = self.find_chunk_size(area)
        if chunk_size is None:
            return False
        try:
            row_number, row_index = self.unused[chunk_size].pop(0)
        except KeyError:
            _fits = False
            total_width = self.w
            end_of_row = len(self.rows[0])
            for row_index, row in enumerate(self.rows):
                if total_width - sum(row[i][1][1] for i in range(len(row))) >= chunk_size[1]:
                    _fits = True
                    row.append((area, chunk_size))
                    break
        else:
            _fits = True
            self.rows[row_number][row_index] = (area, chunk_size)

        if _fits:
            self.grid_position[identifier] = (row_index, len(row))
            width_offset = sum(item[1][1] for item in row[:-1]) if len(row) > 1 else 0#row[0][1][1]
            print width_offset, row
            self.offsets[identifier] = (self.x + width_offset,
                                        self.y + row_index * self.max_size[0])
        return _fits

    def get_position(self, identifier):
        x_offset, y_offset = self.offsets[identifier]
        return self.x + x_offset, self.y + y_offset

    def find_chunk_size(self, area, _cache=dict()):
        w, h = area[2:]
        max_w, max_h = self.max_size
        if w > max_w or h > max_h:
            return None

        for chunk_size in self.chunk_sizes:
            if chunk_size[0] >= w and chunk_size[1] >= h:
                return chunk_size

    def remove_from_atlas(self, identifier):
        row_number, row_index = self.grid_position[identifier]
        del self.grid_position[identifier]

        area, chunk_size = self.rows[row_number][row_index]
        self.rows[row_number][row_index] = (None, chunk_size)
        self.unused[chunk_size].append((row_number, row_index))

        del self.offsets[identifier]


def test(**kwargs):
    return Texture_Atlas(**kwargs)
