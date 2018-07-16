import sqlite3

command = """
	CREATE TABLE [DatabaseInformation] (
	[Version]	INTEGER,
	[CreateDateTime]	INTEGER,
	[OriginalProject]	TEXT
	);
	CREATE TABLE [GeneralInformation] (
	[ID]	INTEGER,
	[Name]	TEXT UNIQUE,
	[Code]	TEXT,
	[Title]	TEXT,
	[Colour]	INTEGER,
	[CreateDateTime]	INTEGER,
	[CreateBy]	TEXT,
	[CreateCompany]	TEXT,
	[EditDateTime]	INTEGER,
	[EditBy]	TEXT,
	[EditCompany]	TEXT,
	[MetaNotes]	TEXT,
	[Accuracy]	INTEGER,
	[XMinimum]	REAL,
	[XMaximum]	REAL,
	[YMinimum]	REAL,
	[YMaximum]	REAL,
	[ZMinimum]	REAL,
	[ZMaximum]	REAL,
	[DTMPlane]	INTEGER,
	[Volume]	REAL,
	[SurfaceArea]	REAL,
	[Validated]	INTEGER,
	[IsLocked]	INTEGER,
	[LockBy]	TEXT,
	[LockReason]	TEXT,
	[LockDateTime]	INTEGER,
	PRIMARY KEY([ID])
	);
	CREATE TABLE [Geometry] (
	[ID]	INTEGER,
	[Geometry]	BLOB,
	PRIMARY KEY([ID])
	);
	CREATE TABLE [PointAttributeDefinition] (
	[ID]	INTEGER,
	[Name]	TEXT,
	[Type]	INTEGER,
	[Precision]	INTEGER,
	[DefaultValueText]	TEXT,
	[DefaultValueInteger]	INTEGER,
	[DefaultValueReal]	REAL,
	PRIMARY KEY([ID])
	);
	CREATE TABLE [PointAttributeValue] (
	[TriangulationID]	INTEGER,
	[AttributeID]	INTEGER,
	[AttributeValues]	BLOB,
	PRIMARY KEY([TriangulationID],[AttributeID]),
	FOREIGN KEY([AttributeID]) REFERENCES [PointAttributeDefinition]([ID]) ON DELETE CASCADE
	);
	CREATE TABLE [TriangleAttributeDefinition] (
	[ID]	INTEGER,
	[Name]	TEXT,
	[Type]	INTEGER,
	[Precision]	INTEGER,
	[DefaultValueText]	TEXT,
	[DefaultValueInteger]	INTEGER,
	[DefaultValueReal]	REAL,
	PRIMARY KEY([ID])
	);
	CREATE TABLE [TriangleAttributeValue] (
	[TriangulationID]	INTEGER,
	[AttributeID]	INTEGER,
	[AttributeValues]	BLOB,
	PRIMARY KEY([TriangulationID],[AttributeID]),
	FOREIGN KEY([AttributeID]) REFERENCES [TriangleAttributeDefinition]([ID]) ON DELETE CASCADE
	);
	CREATE TABLE [UserAttributeDefinition] (
	[ID]	INTEGER,
	[Name]	TEXT,
	[Type]	INTEGER,
	[Precision]	INTEGER,
	[DefaultValueText]	TEXT,
	[DefaultValueInteger]	INTEGER,
	[DefaultValueReal]	REAL,
	PRIMARY KEY([ID])
	);
	CREATE TABLE [UserAttributeValue] (
	[TriangulationID]	INTEGER,
	[AttributeID]	INTEGER,
	[ValueText]	TEXT,
	[ValueInteger]	INTEGER,
	[ValueReal]	REAL,
	PRIMARY KEY([TriangulationID],[AttributeID]),
	FOREIGN KEY([AttributeID]) REFERENCES [UserAttributeDefinition]([ID]) ON DELETE CASCADE
	);
"""

path = 'D:\\new_type.tridb'
connection = sqlite3.connect(path)
cursor = connection.cursor()
cursor.executescript(command)
connection.close()
