class Boundary:
	def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float) -> None:
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax

	def get_boundary_tuple(self) -> tuple:
		return ([self.xmin, self.xmax], [self.ymin, self.ymax])

	def get_boundary_str(self) -> str:
		return f"([{self.xmin}, {self.xmax}], [{self.ymin}, {self.ymax}])"

	def get_boundary_name(self) -> str:
		return f"{self.xmin}_{self.xmax}_{self.ymin}_{self.ymax}
