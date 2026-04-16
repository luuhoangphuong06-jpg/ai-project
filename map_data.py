import osmnx as ox

class MapData:
    """
    Lớp quản lý dữ liệu bản đồ. 
    Chịu trách nhiệm tải đồ thị đường phố và tìm kiếm các ga tàu.
    """
    def __init__(self, center_point=(59.9400, 30.3200), dist=2000):
        self.center_point = center_point
        self.dist = dist
        self.graph = None
        self.load_graph()

    def load_graph(self):
        """Tải mạng lưới đường phố (chỉ dành cho xe cộ) từ OpenStreetMap."""
        print(f"[Data Module] Đang tải bản đồ bán kính {self.dist}m từ tâm {self.center_point}...")
        self.graph = ox.graph_from_point(self.center_point, dist=self.dist, network_type='drive')
        print(f"[Data Module] Đã tải xong! Tổng số điểm giao cắt: {len(self.graph.nodes)}")
    
    def get_graph(self):
        """Trả về đối tượng đồ thị NetworkX cho nhóm Thuật toán sử dụng."""
        return self.graph

    def get_nearest_node(self, lat, lon):
        """
        Tìm ID của ngã tư gần nhất với tọa độ (lat, lon) mà người dùng click chuột.
        """
        if self.graph is None:
            raise ValueError("Đồ thị chưa được tải. Hãy gọi load_graph() trước.")
        # Lưu ý: osmnx nhận tham số X là Kinh độ (lon), Y là Vĩ độ (lat)
        return ox.distance.nearest_nodes(self.graph, X=lon, Y=lat)

    def get_stations(self):
        """
        Quét và trả về danh sách các ga tàu/tàu điện ngầm trong khu vực.
        Trả về: list các dictionary [{'name': 'Tên ga', 'lat': vĩ độ, 'lon': kinh độ}]
        """
        print("[Data Module] Đang quét dữ liệu ga tàu...")
        stations_data = []
        tags = {'railway': 'station', 'station': 'subway'}
        
        try:
            stations = ox.features_from_point(self.center_point, tags=tags, dist=self.dist)
            for idx, row in stations.iterrows():
                centroid = row.geometry.centroid
                station_name = row.get('name', 'Ga Tàu')
                if not isinstance(station_name, str): 
                    station_name = 'Ga Tàu'
                
                stations_data.append({
                    'name': station_name,
                    'lat': centroid.y,
                    'lon': centroid.x
                })
            print(f"[Data Module] Tìm thấy {len(stations_data)} ga tàu.")
        except Exception as e:
            print(f"[Data Module] Lỗi khi quét ga tàu: {e}")
            
        return stations_data