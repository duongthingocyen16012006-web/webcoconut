CREATE TABLE KeoDua (
    id SERIAL PRIMARY KEY,
    ten_keo VARCHAR(100),
    huong_vi VARCHAR(50),
    gia_tien INT
);
INSERT INTO KeoDua (ten_keo, huong_vi, gia_tien) VALUES 
('Kẹo dừa truyền thống', 'Nguyên bản', 30000),
('Kẹo dừa lá dứa', 'Lá dứa', 35000),
('Kẹo dừa đậu phộng', 'Đậu phộng', 40000),
('Kẹo dừa sầu riêng', 'Sầu riêng', 45000);
